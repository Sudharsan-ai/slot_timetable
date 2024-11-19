from http.server import HTTPServer,BaseHTTPRequestHandler
content="""
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
"""
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("Your web server is running....") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()