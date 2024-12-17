import dash                              
from dash import html
from dash import dcc
from dash.dependencies import Output, Input

from dash_extensions import Lottie       
import dash_bootstrap_components as dbc  
import plotly.express as px              
import pandas as pd                      
from datetime import date
import calendar
from wordcloud import WordCloud          


url_coonections = "https://assets9.lottiefiles.com/private_files/lf30_5ttqPi.json"
url_companies = "https://assets9.lottiefiles.com/packages/lf20_EzPrWM.json"
url_msg_in = "https://assets9.lottiefiles.com/packages/lf20_8wREpI.json"
url_msg_out = "https://assets2.lottiefiles.com/packages/lf20_Cc8Bpg.json"
url_reactions = "https://assets2.lottiefiles.com/packages/lf20_nKwET0.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


# Import App data from csv sheets **************************************
df_cnt = pd.read_csv("Dashboard-LinkedIn/data/Connections.csv")
df_cnt["Connected On"] = pd.to_datetime(df_cnt["Connected On"],format="%d-%b-%y")
df_cnt["month"] = df_cnt["Connected On"].dt.month
df_cnt['month'] = df_cnt['month'].apply(lambda x: calendar.month_abbr[x])

df_invite = pd.read_csv("Dashboard-LinkedIn/data/Invitations.csv")
df_invite["Sent At"] = pd.to_datetime(df_invite["Sent At"],format="%m/%d/%y, %I:%M %p")

df_react = pd.read_csv("Dashboard-LinkedIn/data/Reactions.csv")
df_react["Date"] = pd.to_datetime(df_react["Date"], format="%m/%d/%Y %H:%M")

df_msg = pd.read_csv("Dashboard-LinkedIn/data/messages.csv")
df_msg["DATE"] = pd.to_datetime(df_msg["DATE"])

#* Bootstrap themes: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

#Allows Render to run the application correctly
server = app.server

app.layout = dbc.Container([

    #* Main Content
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='/assets/linkedin.png') # 150px by 45px
            ],className='mb-2'),
            dbc.Card([
                dbc.CardBody([
                    dbc.CardLink("LinkedIn", target="_blank",
                                     href="https://www.linkedin.com/"
                        )
                ])
            ]),
        ], width=2),

        #* Titel
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.CardHeader(html.H3("LinkedIn Connections Analytics", className='font-weight-bold'),
                                             style={
                                            'textAlign': 'center', 
                                             'backgroundColor': '#0077B5',  # LinkedIn blue
                                             'color': 'white'  # White text
            }),
            html.Div(style={'paddingTop': '20px'}),  # Paddin between date-pickers and title

            dcc.DatePickerSingle(
                        id='my-date-picker-start',
                        date=date(2018, 1, 1),
                        className='ml-5'
                    ),
                    dcc.DatePickerSingle(
                        id='my-date-picker-end',
                        date=date(2021, 4, 4),
                        className='mb-2 ml-2'
                    ),
            ]),
    
            ],color="#0077B5", className='mb-2'),
        ], width=8),


        dbc.Col([
            #* Sidebar
            dbc.Card([
                dbc.CardHeader(html.H5("List of Graphs", className='font-weight-bold'),
                               style={'textAlign':'center',
                                      'backgroundColor': '#0077B5',  # LinkedIn blue
                                      'color': 'white'  # White text
                                      }),
                dbc.CardBody([
                    #html.A creates an anchor link to same page, the class name removes unterstriechen
                    html.A("Total Connections by Month link", href="#connections-chart", className="list-group-item list-group-item-action"),
                    html.Br(),
                    html.A('Total Connections by Month',href="#connections-chart", className="list-group-item list-group-item-action"),
                    html.Br(),
                    html.A("Total Connections by Company\n",href="#connections-chart", className="list-group-item list-group-item-action"),
                    html.Br(),
                    html.A("Empty Graph", href="#connection-empty-chart",className="list-group-item list-group-item-action"),
                    html.Br(),
                    html.A("Messages Sent & Received", href="#connection-empty-chart", className="list-group-item list-group-item-action"),
                    html.Br(),
                    html.A("Total Connections by Position", href="#connection-empty-chart", className="list-group-item list-group-item-action"),
                    html.Br(),
                    html.A("Messages per Month/Date", href="#connection-stacked-chart", className="list-group-item list-group-item-action"),                
                ], style={'textAlign':'left'})
            ], color="white", style={'height':'90vh'}),
        ], width=2,style={'position': 'absolute', 'top': '10', 'right': '0', 'z-index': '1000'}),
    ],className='mb-2 mt-2'),
    #**
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="67%", height="67%", url=url_coonections)),
                dbc.CardBody([
                    html.H6('Connections'),
                    html.H2(id='content-connections', children="000")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="32%", height="32%", url=url_companies)),
                dbc.CardBody([
                    html.H6('Companies'),
                    html.H2(id='content-companies', children="000")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="25%", height="25%", url=url_msg_in)),
                dbc.CardBody([
                    html.H6('Invites received'),
                    html.H2(id='content-msg-in', children="000")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="53%", height="53%", url=url_msg_out)),
                dbc.CardBody([
                    html.H6('Invites sent'),
                    html.H2(id='content-msg-out', children="000")
                ], style={'textAlign': 'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="25%", height="25%", url=url_reactions)),
                dbc.CardBody([
                    html.H6('Reactions'),
                    html.H2(id='content-reactions', children="000")
                ], style={'textAlign': 'center'})
            ]),
        ], width=2),
    ],className='mb-2'),
    
    #** Charts start
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='line-chart', figure={}, config={'displayModeBar': False}), # ensures that the ModeBar (toolbar) is hidden.
                ])
            ]),
        ], width=6 , id='connections-chart'),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='bar-chart', figure={}, config={'displayModeBar': False}),
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
    dbc.Row([
        #* Fourth Row
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
            
                    dcc.Graph(id='TBD', figure={}),
                ])
            ]),
        ], width=3, id='connection-empty-chart'),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='pie-chart', figure={}, config={'displayModeBar': False}),
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='wordcloud', figure={}, config={'displayModeBar': False}),
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
    dbc.Row([
        dbc.Col([
            #* In this column, I will store my own chart: Stacked Area Chart
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='Stacked-Area-Message/Month', figure={}, config={'displayModeBar': False}), # ensures that the ModeBar (toolbar) is hidden.
                ])
            ]),
        ], width=10, id='connection-stacked-chart'),
    
    ],className='mb-2'),
], fluid=True)


# Updating the 5 number cards ******************************************
@app.callback(
    Output('content-connections','children'),
    Output('content-companies','children'),
    Output('content-msg-in','children'),
    Output('content-msg-out','children'),
    Output('content-reactions','children'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)
def update_small_cards(start_date, end_date):
    # Connections
    dff_c = df_cnt.copy()

    dff_c = dff_c[(dff_c['Connected On']>=start_date) & (dff_c['Connected On']<=end_date)]
    conctns_num = len(dff_c)
    compns_num = len(dff_c['Company'].unique())

    # Invitations
    dff_i = df_invite.copy()
    dff_i = dff_i[(dff_i['Sent At']>=start_date) & (dff_i['Sent At']<=end_date)]
    # print(dff_i)
    in_num = len(dff_i[dff_i['Direction']=='INCOMING'])
    out_num = len(dff_i[dff_i['Direction']=='OUTGOING'])

    # Reactions
    dff_r = df_react.copy()
    dff_r = dff_r[(dff_r['Date']>=start_date) & (dff_r['Date']<=end_date)]
    reactns_num = len(dff_r)

    return conctns_num, compns_num, in_num, out_num, reactns_num


# start_date = pd.to_datetime("2021-01-04").tz_localize("UTC")
# end_date = pd.to_datetime("2021-08-04").tz_localize("UTC")
# start_date = pd.to_datetime("2021-01-04")
# end_date = pd.to_datetime("2021-08-04")

@app.callback(
    Output('line-chart', 'figure'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def update_line(start_date, end_date):
    dff = df_cnt.copy()
    
    # Step 1: Filter data within the specified date range
    dff = dff[(dff['Connected On'] >= start_date) & (dff['Connected On'] <= end_date)]
    
    # Count connections per month
    dff = dff[["month"]].value_counts().to_frame().reset_index()
    
    dff.rename(columns={'count': 'Total connections'}, inplace=True) # actually no need to do this
    
    # Create the line chart
    fig_line = px.line(dff, x='month', y='Total connections', template='ggplot2',
                       title="Total Connections by Month Name")
    fig_line.update_traces(mode="lines+markers", fill='tozeroy', line={'color': 'blue'})
    fig_line.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    
    return fig_line


#>> Stacked Area Chart **************************************************
@app.callback(
        Output('Stacked-Area-Message/Month', 'figure'),
        Input('my-date-picker-start', 'date'),
        Input('my-date-picker-end', 'date'),
)
def update_stacked(start_date, end_date):
    dff = df_msg.copy()
    # Select valid dates
    dff = dff[(dff['DATE'] >= start_date) & (dff['DATE'] <= end_date)]

    #>> Filter data we need
    dff['month'] = dff['DATE'].dt.month_name()
    dff['day'] = dff['DATE'].dt.day_name()
    dff = dff.groupby(['month', 'day']).size().reset_index(name='Total')

    # Define month order -> Returns a string with all month names
    month_list = list(calendar.month_name)[1:]

    dff = dff.sort_values(by='Total', ascending=False)
    #

    #>> Create the stacked area chart
    fig_stacked = px.area(dff, x='month', y='Total', color='day', template='ggplot2',
                          title="Messages per Month/Day",
                        category_orders={"month": month_list})
    fig_stacked.update_layout(margin=dict(l=20, r=20, t=30, b=20), 
                              xaxis={
            'categoryorder': 'array', 
            'categoryarray': month_list 
            #>> ensures that months are plotted in the exact order defined in month_list, 
            #>> even if some months are missing from the dataset.
        })
    return fig_stacked



# Bar Chart ************************************************************
@app.callback(
    Output('bar-chart','figure'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)
def update_bar(start_date, end_date):
    dff = df_cnt.copy()
    # filter
    dff = dff[(dff['Connected On']>=start_date) & (dff['Connected On']<=end_date)]
    dff = dff[["Company"]].value_counts().head(6) # top 6
    dff = dff.to_frame()
    dff.reset_index(inplace=True)
    dff.rename(columns={'count':'Total connections'}, inplace=True)

    fig_bar = px.bar(dff, x='Total connections', y='Company', template='ggplot2',
                      orientation='h', title="Total Connections by Company")
    fig_bar.update_yaxes(tickangle=45)
    fig_bar.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig_bar.update_traces(marker_color='blue')

    return fig_bar


# Pie Chart ************************************************************
@app.callback(
    Output('pie-chart','figure'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)
def update_pie(start_date, end_date):
    dff = df_msg.copy()
    dff = dff[(dff['DATE']>=start_date) & (dff['DATE']<=end_date)]
    msg_sent = len(dff[dff['FROM']=='Adam Schroeder'])
    msg_rcvd = len(dff[dff['FROM'] != 'Adam Schroeder'])
    fig_pie = px.pie(names=['Sent','Received'], values=[msg_sent, msg_rcvd],
                     template='ggplot2', title="Messages Sent & Received"
                     )
    fig_pie.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig_pie.update_traces(marker_colors=['lightblue','lightcoral'])

    return fig_pie


# Word Cloud ************************************************************
@app.callback(
    Output('wordcloud','figure'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)
def update_pie(start_date, end_date):
    dff = df_cnt.copy()
    dff = dff.Position[(dff['Connected On']>=start_date) & (dff['Connected On']<=end_date)].astype(str)

    # initializes a word cloud generator 
    
    """
    generate method takes a single string as input, which is expected to be a concatenated sequence of words or text.
    It processes the input text to calculate the frequency of each word, 
    and then creates a visual representation (the word cloud) where:
    Words with higher frequencies appear larger.
    Words with lower frequencies appear smaller.
    """
    
    my_wordcloud = WordCloud(
        background_color='white',
        height=275
    ).generate(' '.join(dff))

    fig_wordcloud = px.imshow(my_wordcloud, template='ggplot2',
                              title="Total Connections by Position")
    fig_wordcloud.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig_wordcloud.update_xaxes(visible=False)
    fig_wordcloud.update_yaxes(visible=False)

    return fig_wordcloud


if __name__=='__main__':
    app.run_server(debug=True, port=8005)
