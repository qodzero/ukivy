from kivy.uix.button import Button
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ObjectProperty
from kivy.graphics import Color, Rectangle, RoundedRectangle, Ellipse
from kivy.lang import Builder

Builder.load_string('''
<FlatButton>:
    background_normal: ''
    background_color: [0,0,0,0]
    text_size: self.size
    valign: 'middle'
    halign: 'center'
    markup: True
''')

class RoundedButton(FlatButton):
    radius = NumericProperty(10)

    def update_back(self):
        with self.canvas.before:
            self.color = Color(rgba=self.background_color)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=self.radius)

    def on_radius(self, _, value):
        """When the radius is set/changed, this function
        is called to update the radius of the button on the
        canvas

        Parameters
        ----------
        _ : widget
            This is usually the instance calling the function,
            we dont care about this
        value : number
            The value of the radius property

        Returns
        -------
        None
        """
        self.rect.radius = value




class FlatButton(Button):
    """A normal ::class `kivy.uix.button.Button` with all
    the visual representations removed, this button
    basically just looks like a label, but ofcourse, unlike
    a label, its clickable.
    Since this inherits from a normal Button, it
    supports all of its properties.

    Usage
    ---------

    from ukivy.button import FlatButton

    ...

    btn = FlatButton(text='myButton')
    some_widget.add_widget(btn)

    ...
    """
    pass
