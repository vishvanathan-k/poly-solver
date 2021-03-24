import wpf
from System.Windows import Application, Window
import cmath as m
class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'PolynomialSolver.xaml')
    def ButtonClicked(self, sender, e):
        a = int(self.textBox.Text)
        b = int(self.textBox1.Text)
        c = int(self.textBox2.Text)
        d = ((b**2) - 4*a*c)
        el = m.sqrt(d)
        alpha = ((-b + el)/(2*a)) 
        beta = ((-b - el)/(2*a))
        self.textBox3.Text = str(alpha)
        self.textBox4.Text = str(beta)
        pass   

if __name__ == '__main__':
    Application().Run(MyWindow())
