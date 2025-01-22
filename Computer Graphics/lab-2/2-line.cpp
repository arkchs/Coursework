#include<GL/glut.h>


void display() {
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.0, 1.0, 0.0);
	glLineWidth(2.0);
	glBegin(GL_LINES);
	glVertex2f(10.0,10.0);
	glVertex2f(50.0, 50.0);
	glEnd();
	glFlush();
}

void myinit() {
	glClearColor(0.0, 0.0, 0.0, 1.0)	;
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0.0, 499.0, 0.0, 499.0);
}
//change gl clear color 2(i)
//modify void main by replacing 'Blank Window' with Colored Window or whatever it is just the title

void main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("Line");
	glutDisplayFunc(display);
	myinit();
	glutMainLoop();

}