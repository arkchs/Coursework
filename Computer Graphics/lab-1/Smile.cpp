#include<GL/glut.h>
#include<cmath>
//Making a Smile using a Rectangle and two Circles
void rectangle(int startX, int startY, int length, int width) {
	glColor3f(1.0,0.0,0.0);
	glBegin(GL_POLYGON);

	glVertex2f(startX, startY);
	glVertex2f(startX+length, startY);
	glVertex2f(startX+length, startY+width);
	glVertex2f(startX, startY+length);


	glEnd();

}
void circle(float centerX, float centerY, float radius) {
	glColor3f(1.0,1.0,0.0);
	glBegin(GL_POLYGON);
	
	int numSegments = 100;

	for (int i = 0;i < numSegments; i++) {
		float angle = 2 * 3.1415f * i / numSegments;
		float x = radius * cos(angle);
		float y = radius * sin(angle);
		glVertex2f(centerX + x, centerY + y);

	}
	glEnd();
}
void display() {
	glClear(GL_COLOR_BUFFER_BIT);
	rectangle(200, 100, 50,50);
	circle(300,300,50);
	circle(150, 300, 50);
	glFlush();
}


void myinit() {
	glClearColor(0.0,0.0,0.0, 1.0); //Background 
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0.0, 499.0, 0.0, 499.0);
}
int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(0, 0);// where the display window will appear
	glutCreateWindow("Point"); // display window name
	glutDisplayFunc(display); //calling the function call display
	myinit();
	glutMainLoop();

}