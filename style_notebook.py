# style the notebook
from IPython.core.display import HTML
import urllib.request
# this link is to my Kalman filter book CSS file.
response = urllib.request.urlopen('http://bit.ly/1LC7EI7')
HTML(response.read().decode("utf-8"))