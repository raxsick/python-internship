
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sanjay Kumar - Resume</title>
    </head>
    <body style="font-family: Arial, sans-serif; background:#f5f7fa; margin:0; padding:20px;">

        <div style="
        max-width:900px; 
        margin:auto; 
        background:white; 
        padding:25px; 
        border-radius:10px; 
        box-shadow:0 0 10px rgba(0,0,0,0.1);
       ">

            <!-- Name -->
            <h1 style="margin-bottom:5px; color:#333;">Sanjay Kumar</h1>

            <!-- Contact -->
            <p style="margin:0; color:#555;">
               📞 6299943151 <br>
               📧 Sanjaykne79@gmail.com <br>
               📍 India
           </p>

           <!-- Profile Summary -->
           <h2 style="margin-top:30px; border-bottom:2px solid #ddd; padding-bottom:5px; color:#444;">
               Profile Summary
           </h2>
           <p style="line-height:1.6; color:#555;">
               Passionate learner with strong interest in programming and creative arts.
               Skilled in C programming, Java, and Python. Enjoys music and art along with 
               technical learning. Highly motivated and eager to explore new technologies.
           </p>

           <!-- Skills -->
           <h2 style="margin-top:30px; border-bottom:2px solid #ddd; padding-bottom:5px; color:#444;">
               Skills
           </h2>

           <div style="margin-bottom:20px;">
                <span style="
                   background:#e3e9f1; 
                   padding:8px 15px; 
                   border-radius:5px; 
                   margin:5px; 
                   display:inline-block;
               ">C Programming</span>

               <span style="
                   background:#e3e9f1; 
                   padding:8px 15px; 
                   border-radius:5px; 
                   margin:5px; 
                   display:inline-block;
               ">Java</span>

               <span style="
                   background:#e3e9f1; 
                   padding:8px 15px; 
                   border-radius:5px; 
                   margin:5px; 
                   display:inline-block;
                ">Python</span>
         </div>

              <!-- Interests -->
               <h2 style="margin-top:30px; border-bottom:2px solid #ddd; padding-bottom:5px; color:#444;">
               Interests
            </h2>
           <p style="line-height:1.6; color:#555;">Music, Art</p>

           <!-- Education -->
           <h2 style="margin-top:30px; border-bottom:2px solid #ddd; padding-bottom:5px; color:#444;">
               Education
           </h2>
           <p style="color:#555;">Add your college/school details here</p>

           <!-- Projects -->
           <h2 style="margin-top:30px; border-bottom:2px solid #ddd; padding-bottom:5px; color:#444;">
               Projects
           </h2>
           <p style="line-height:1.6; color:#555;">
               You can list your C, Java, and Python projects here.
           </p>

       </div>

   </body>
   </html>
   """

@app.route("/about")
def abouta():
    return """
<h1/> i am home page </h1>
<h2/> i running page </h2> """
if __name__ == "__main__":
    app.run(debug=True)
