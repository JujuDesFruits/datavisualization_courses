{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import plotly.graph_objects as go\n",
    "import dash\n",
    "from dash import dcc\n",
    "from dash import html\n",
    "from dash.dependencies import Input, Output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', \n",
    "                            encoding = \"ISO-8859-1\",\n",
    "                            dtype={'Div1Airport': str, 'Div1TailNum': str, \n",
    "                                   'Div2Airport': str, 'Div2TailNum': str})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# add callback decorator\n",
    "@app.callback( Output(component_id='line-plot', component_property='figure'),\n",
    "               Input(component_id='input-year', component_property='value'))\n",
    "# Add computation to callback function and return graph\n",
    "def get_graph(entered_year):\n",
    "    # Select 2019 data\n",
    "    df =  airline_data[airline_data['Year']==int(entered_year)]\n",
    "    \n",
    "    # Group the data by Month and compute average over arrival delay time.\n",
    "    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()\n",
    "    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))\n",
    "    fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')\n",
    "    return fig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x24888391720>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run_server()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
