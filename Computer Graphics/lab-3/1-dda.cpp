#include<GL/glut.h>
void dda(float x1, float y1, float x2, float y2) {
	float dx = x2 - x1;
	float dy = y2 - y1;

	float x = 0;
	float slope = dy / dx;
	glVertex2f(x1, y1);
	for (float i = x1;i <= x2;i++) {
		x = i;
		float y = y1 + slope * (x - x1);
		glVertex2f(x, y);
	}

}

void display() {
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0,1.0,1.0);

	glBegin(GL_POINTS);
	dda(100.0,100.0, 300.0,300.0);
	glEnd();

	glFlush();
}

void myinit() {
	glClearColor(0.0, 0.0, 0.0, 1.0);
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
	glutCreateWindow("DDA");
	glutDisplayFunc(display);
	myinit();
	glutMainLoop();

}