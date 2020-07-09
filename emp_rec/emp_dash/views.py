from bokeh.plotting import figure
from bokeh.embed import components
from django.template.response import TemplateResponse


def get_figure(wd,ht,title,tooltips):
    pd_default = figure(plot_width=wd, plot_height=ht,tools="", title = title,tooltips=tooltips)
    pd_default.border_fill_color = None
    pd_default.background_fill_color = None
    pd_default.background_fill_alpha = 0.5
    pd_default.outline_line_color = None
    pd_default.toolbar.autohide = True
    pd_default.axis.major_label_text_color = None#'white'
    pd_default.axis.axis_line_color = None
    pd_default.axis.minor_tick_line_color = None
    pd_default.grid.visible = False
    pd_default.axis.major_tick_line_color = None
    pd_default.title.text_color = "white"
    return pd_default
TOOLTIPS=[]
def dashboard(request):
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]
    plot = get_figure(400,300,'Name',TOOLTIPS)
    plot.annular_wedge
    plot.line(x, y, line_width=2)
    script, div = components(plot)

    return TemplateResponse(request, 'base.html',{'script': script, 'div': div}).render()
