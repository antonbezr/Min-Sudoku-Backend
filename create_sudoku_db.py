#!/usr/bin/python
import mysql.connector
import numpy as np
from itertools import permutations 


def getUniqueSudokus(raw_path, total):
   sudoku = np.zeros(0)
   sudokuPatterns = np.zeros(0)
   data = np.loadtxt(raw_path, delimiter=',', dtype=str)
   index = 0
   while (sudoku.size < total):
      puzzle = data[index][0]
      puzzle = puzzle.replace('.', '0')
      test = puzzle
      for i in range(1, 10): test = test.replace(str(i), 'x')
      if (sudoku.size == 0 or test not in sudokuPatterns): 
         sudoku = np.append(sudoku, puzzle)
         sudokuPatterns = np.append(sudokuPatterns, test)
      index += 1
   return sudoku


def uploadSudokus(easy, medium, hard):
   print('Connecting to the MySQL database...')
   conn = mysql.connector.connect(
      host="",
      user="",
      password="",
      database=""
   )
   cur = conn.cursor()
   cur.execute('DROP TABLE IF EXISTS easy')
   cur.execute('DROP TABLE IF EXISTS medium')
   cur.execute('DROP TABLE IF EXISTS hard')
   cur.execute('CREATE TABLE easy (id INT NOT NULL, board VARCHAR(81) NOT NULL, PRIMARY KEY (id))')
   cur.execute('CREATE TABLE medium (id INT NOT NULL, board VARCHAR(81) NOT NULL, PRIMARY KEY (id))')
   cur.execute('CREATE TABLE hard (id INT NOT NULL, board VARCHAR(81) NOT NULL, PRIMARY KEY (id))')
   print("Inserting Sudoku boards...")
   for i in range(len(easy)):
      query = 'INSERT INTO easy (id, board) VALUES (\'' + str(i + 1) + '\',' + ' \'' + easy[i] + '\')'
      cur.execute(query)
   for i in range(len(medium)):
      query = 'INSERT INTO medium (id, board) VALUES (\'' + str(i + 1) + '\',' + ' \'' + medium[i] + '\')'
      cur.execute(query)
   for i in range(len(hard)):
      query = 'INSERT INTO hard (id, board) VALUES (\'' + str(i + 1) + '\',' + ' \'' + hard[i] + '\')'
      cur.execute(query)
   conn.commit()
   cur.close()
   conn.close()
   print('Database connection closed.')


def deleteCustom():
   print('Connecting to the MySQL database...')
   conn = mysql.connector.connect(
      host="",
      user="",
      password="",
      database=""
   )
   cur = conn.cursor()
   cur.execute('DROP TABLE IF EXISTS custom')
   cur.execute('CREATE TABLE custom (id INT NOT NULL, board VARCHAR(81) NOT NULL, difficulty VARCHAR(255) NOT NULL, generated INT NOT NULL, PRIMARY KEY (id))')
   conn.commit()
   cur.close()
   conn.close()
   print('Database connection closed.')


easy = getUniqueSudokus('generated/easy.txt', 1000)
medium = getUniqueSudokus('generated/medium.txt', 1000)
hard = getUniqueSudokus('generated/hard.txt', 1000)

uploadSudokus(easy, medium, hard)
deleteCustom()