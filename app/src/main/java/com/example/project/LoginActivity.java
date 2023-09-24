package com.example.project;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class LoginActivity extends AppCompatActivity {

    private EditText courseNameEdt, courseDescriptionEdt;
    private Button addCourseBtn;
    private DBHandler dbHandler;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        courseNameEdt = findViewById(R.id.idEdtCourseName);
        courseDescriptionEdt = findViewById(R.id.idEdtCourseDuration);
        addCourseBtn = findViewById(R.id.idBtnAddCourse);


            // initializing all our variables.
            courseNameEdt = findViewById(R.id.idEdtCourseName);

            addCourseBtn = findViewById(R.id.idBtnAddCourse);

            // creating a new dbhandler class
            // and passing our context to it.
            dbHandler = new DBHandler(LoginActivity.this);

            // below line is to add on click listener for our add course button.
            addCourseBtn.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {

                    // below line is to get data from all edit text fields.
                    String courseName = courseNameEdt.getText().toString();

                    String courseDescription = courseDescriptionEdt.getText().toString();


                    // validating if the text fields are empty or not.
                    if (courseName.isEmpty() && courseDescription.isEmpty()) {
                        Toast.makeText(LoginActivity.this, "Please enter all the data..", Toast.LENGTH_LONG).show();
                        return;
                    }

                    // on below line we are calling a method to add new
                    // course to sqlite data and pass all our values to it.
                    LoginHandler.addNewCourse(courseName);

                    // after adding the data we are displaying a toast message.
                    Toast.makeText(LoginActivity.this, courseName, Toast.LENGTH_LONG).show();
                    courseNameEdt.setText("");

                    courseDescriptionEdt.setText("");
                }
            });
        }

    }
