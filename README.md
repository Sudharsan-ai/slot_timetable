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
    <img src="logo.png" width="800"><br><br>
    
   <table> <tr><td></td><td>SLOT TIME TABLE -SUDHARSAN S (24900437)</td></table>
    <table border="5"  width="50%" align="center" bgcolor="cyan">

      <tr>
         <th bgcolor="yellow">DAY/TIME</th>
         <th bgcolor="yellow">MONDAY</th>
         <th bgcolor="yellow">TUESDAY</th>
         <th bgcolor="yellow">WEDNESDAY</th>
         <th bgcolor="yellow">THURSDAY</th>
         <th bgcolor="yellow">FRIDAY</th>
         <th bgcolor="yellow">SATURDAY</th>
      </tr>

     
      <tr align="center">
         
         <td bgcolor="yellow">8:00AM-10:00AM</td> 
         <td>-</td> 
         <td bgcolor="green" style="color:aliceblue">BEE</td> 
         <td bgcolor="white" style="color:black">PYTHON</td> 
         <td>-</td>
         <td>-</td>
         <td>-</td>

      </tr>
      <tr align="center">
         <td bgcolor="yellow">10:00AM-12:00PM</td> 
         <td bgcolor="white" style="color:black">PYTHON</td> 
         <td bgcolor="brown"style="color:aliceblue"> DE </td> 
         <td bgcolor="green"style="color:aliceblue"> BEE </td> 
         <td>-</td>
         <td bgcolor="orange" style="color:aliceblue"> MATH</td>
         <td bgcolor="blue" style="color:aliceblue"> FWAD </td>
      </tr>
      <tr>
         <td bgcolor="yellow">12:00PM-1:00pm</td>
         <td align="center" COLSPAN="6">LUNCH BREAK
         </td>
 
      </tr>

      <tr align="center">
      <td bgcolor="yellow">1:00PM-3:00AM</td> 
      <td bgcolor="gray" style="color:aliceblue">HV&PE</td> 
      <td bgcolor="blue" style="color:aliceblue">FWAD</td> 
      <td>MENTOR</td> 
      <td bgcolor="blue" style="color:aliceblue">FWAD</td>
      <td bgcolor="brown" style="color:aliceblue">DE</td>
      <td bgcolor="orange" style="color:aliceblue">MATH</td>

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
![alt text](<Screenshot 2024-11-19 183916.png>)
## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
