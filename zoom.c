#include<GL/glut.h>
#include<stdio.h>

//GLfloat angle= 0.0;
//double scale_by_key=0;

int choice;
int i;
double scale_x=1;
double scale_y=1;
double translate_x = 0;
double translate_y = 0;
double temp = 0;

void drawTeapot(){
	glScalef( scale_x,scale_x,1.0f ); 
	glTranslatef(temp,translate_y,1.0f);
	glutSolidTeapot(1);
}

void display(void){
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
	glLoadIdentity();
	gluLookAt(0.0,0.0,5.0,0.0,0.0,0.0,0.0,1.0,0.0);
	/*glScalef( scale_x,scale_x,1.0f ); // to scale the size
	glTranslatef(translate_x,translate_y,1.0f);*/
	temp = translate_x;
	for(i=0;i<choice;i++){
		drawTeapot();
		if(i<(choice/2))
			temp = translate_x/2;
		else 
			temp = -translate_x;
	}	
	glutSwapBuffers();
}

void initRendering(){
    glEnable(GL_DEPTH_TEST);
}

void keyboard(int key,int x, int y){
	printf("keyCode: %d x: %d y: %d\n", key, x, y);
	scale_x=1;
	scale_y=1;
	if (key==27) exit(0);
	switch(key){
		case 107: scale_x = scale_x;
				  scale_y = scale_y;
				  translate_x = 0;
				  choice = 1;
		break;
		case 103: scale_x = scale_x/2;
				  scale_y = scale_y/2;
				  translate_x = 3;
				  choice =2;
		break;
		case 105:scale_x = scale_x/4;
				  scale_y = scale_y/4;
				  translate_x = 2;
				  choice = 3;
		break;
		case 100:scale_x = scale_x/8;
				  scale_y = scale_y/8;
				  translate_x = 1;
				  choice = 4;
		break;
		default: exit(0);
	}
    glutPostRedisplay();
}
void reshape (int w, int h){
	glViewport (0, 0, (GLsizei) w, (GLsizei) h);
	glMatrixMode (GL_PROJECTION);
	glLoadIdentity ();
	gluPerspective (60,(GLfloat)w/(GLfloat)h, 1.0, 100.0);
	glMatrixMode (GL_MODELVIEW); 
}

int main(int argc,char **argv){
	glutInit (&argc,argv);
	glutInitWindowSize(1000,1000);
	glutInitWindowPosition(100,100);
    glutInitDisplayMode(GLUT_DOUBLE);
	glutCreateWindow("teapot");
	glutDisplayFunc (display);
	glutReshapeFunc (reshape);
    initRendering();
    glutSpecialFunc(keyboard);
	glutMainLoop();
	return 0;
}
