Kivy Utils
==============

This is a repository containing some custom widgets I usually use in most,
if not all, of my kivy projects.

Installation
----------------

Sadly For Now You Will Have To Clone The Repo And Put It On Your
Project Directory, Will Probably Add It To PYPI Soon ;)


Example Usage
----------------

```python
from ukivy.button import RoundedButton

rbtn = RoundedButton()
rbtn.radius = 10 # the roundness of the button
rbtn.text = 'Round Button'

some_widget.add_widget(rbtn)
```
And In KV
```
#: import RoundedButton ukivy.button.RoundedButton

RoundedButton:
    text: 'Rounded Baby'
    radius: 30 # value is in pixels by the way
```

# Contributions

Feel Free To Contribute Anything Here As Long As Its Useful
