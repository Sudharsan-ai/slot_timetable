# Ex03 Time Table
## Date:19-11-2024

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and inert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## PROGRAM
```
<html>
  <head>
    <title>
      Slot_Timetable
    </title>
  </head>
  <center>
  <body>
    <img src="C:\Users\sutha\Documents\FIRSTSEM\FWAD\SLOT-EX-3\logo.png" width="800"><br><br>
   <table> <tr><td></td><td>SLOT TIME TABLE -SUDHARSAN S (24900437)</td></table>
    <table border="5" bgcolor="cyan">
      <tr>
        <th bgcolor="yellow">Day/Time</th>
        <th bgcolor="yellow">Monday</th>
        <th bgcolor="yellow">Tuesday</th>
        <th bgcolor="yellow">Wednesday</th>
        <th bgcolor="yellow">Thursday</th>
        <th bgcolor="yellow">Friday</th>
      </tr>

      <tr align="center">
        <th bgcolor="yellow">8-10</th>
        <td colspan="3">FREE SLOT</td>
        <td>BEE</td>
        <td>PY.MODULE</td> 
      </tr>

      <tr align="center">
        <th bgcolor="yellow">10-12</th>
        <td>TAMIL</td>
        <td>FREE SLOT</td>
        <td>FWAD</td>
        <td>FWAD</td>
        <td>BEEE</td>
      </tr>

      <tr align="center">
        <th bgcolor="yellow">12-1</th>
        <td colspan="5">LUNCH</td>
      </tr>

      <tr align="center">
        <th bgcolor="yellow">1-3</th>
        <td colspan="2">FREE SLOT</td>
        <td>MAT</td>
        <td>MATH</td>
        <td>DE</td>
      </tr>

      <tr align="center">
        <th bgcolor="yellow">3-5</th>
        <td colspan="2">FREE SLOT</td>
        <td>TAMIL</td>
        <td>BEEE</td>
        <td>FWAD</td>
      </tr>
    </table><br><br>

    <table border="5">

      <tr>
        <th>
          S.No
        </th>
        <th>
          Subject Code
        </th>
        <th>
          Subject Name
        </th>
      </tr>


      <tr>
        <th>
          1.
        </th>
        <th>
          19AI414
        </th>
        <th>
          Fundamentals of Web Application Development(FWAD)
        </th>
      </tr>


      <tr>
        <th>
          2.
        </th>
        <th>
          19MA201
        </th>
        <th>
          Calculas and Matrix Algebra(MAT)
        </th>
      </tr>

      <tr>
        <th>
         3.
        </th>
        <th>
          19AI301
        </th>
        <th>
          Python Programming(PYTHON)
        </th>
      </tr>

      <tr>
        <th>
          4.
        </th>
        <th>
          SH7101
        </th>
        <th>
          Heritage Of Tamils(TAMIL)
        </th>
      </tr>

      <tr>
        <th>
          5.
        </th>
        <th>
          19EE305
        </th>
        <th>
          Basic Electrical ,Electronics and Measurment Engineering(BEEE)
        </th>
      </tr>

      <tr>
        <th>
          6.
        </th>
        <th>
          19EE404
        </th>
        <th>
          Digital Electronics(DE)
        </th>
      </tr>
      </tr>
    </table>
  </body>
</center>
</html>
```
## OUTPUT
![alt text](<Screenshot 2024-11-19 171655.png>)
## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
