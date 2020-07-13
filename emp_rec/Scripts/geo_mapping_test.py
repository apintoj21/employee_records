import psycopg2
import pgeocode
from bokeh.plotting import figure, show
from bokeh.palettes import Paired
from bokeh.transform import cumsum
from bokeh.models import HoverTool, Legend
from math import pi, ceil
import pandas as pd


def get_figure(wd, ht, title, tooltips, x_range=None, y_range=None):
    if x_range or y_range:
        pd_default = figure(x_range=x_range, y_range=y_range, plot_width=wd, plot_height=ht, tools="",
                            title=title, tooltips=tooltips)
    else:
        pd_default = figure(plot_width=wd, plot_height=ht, tools="", title=title, tooltips=tooltips)
    pd_default.border_fill_color = None
    pd_default.background_fill_color = None
    pd_default.background_fill_alpha = 0.5
    pd_default.outline_line_color = None
    pd_default.toolbar.autohide = True
    pd_default.axis.major_label_text_color = None
    pd_default.axis.axis_line_color = None
    pd_default.axis.minor_tick_line_color = None
    pd_default.grid.visible = False
    pd_default.axis.major_tick_line_color = None
    pd_default.title.text_color = "black"
    return pd_default


def round_up(num, divisor):
    return ceil(num / divisor) * divisor


try:
    connection = psycopg2.connect("host=localhost dbname=emp_db user=postgres password=ajp-21")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select city,zip from emp_rec"
    cursor.execute(postgreSQL_select_Query)
    zip_values = cursor.fetchall()
#     print(zip_values)

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

x = dict(zip_values)
# print(x)
country = pgeocode.Nominatim('us')

data = pd.Series(x).reset_index(name='zip').rename(columns={'index': 'city'})
zip_val = list(data['zip'])
longitude = []
latitude = []
for z in zip_val:
    location = country.query_postal_code(z)
    print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

    # print(zip_val)
    # data['longitude'] = country.query_postal_code(data['zip'])
    # print(data)