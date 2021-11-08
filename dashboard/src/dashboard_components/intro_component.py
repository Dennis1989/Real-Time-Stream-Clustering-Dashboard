import dash_html_components as html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import requests


def intro_layout():

    card = dbc.Card(
    [
       html.Div(
    [
         dbc.Button(
            [html.Div("Allgemeine Informationen",style={"display": "inline-block", "margin-right":"5px"}), html.Div(className="fa fa-lg fa-angle-down")],
            id="collapse-button",
            className="mb-3 mr-1",
            n_clicks=0,
            style ={"color":"white",'background-color': '#182637'}
        ),
    ]),
        dbc.Collapse(
        dbc.CardBody(
            [
                html.Div(id="introTextWrapper",
                    children=dcc.Tabs([
                        dcc.Tab(id="test1234",label='Methodik', children=[
                             dcc.Markdown('''
                                Zur Entdeckung der Themen werden nicht einfach Hashtags ausgewertet und deren Häufigkeit angegeben (wie in den Trends bei Twitter). Wir wenden den an der WWU Münster entwickelten Algorithmus **textClust** an –  eine Methode zum sog. **Echtzeit-Clustering von Twitter Datenströmen**.

                                *Der Algorithmus - Vom Cluster zum Thema:*

                                > Der Algorithmus untersucht in Echtzeit alle eingehenden Tweets, öffentliche Direktnachrichten und Quotes (keine Retweets) aus dem
                                > fortlaufenden Twitter-Datenstrom auf inhaltliche Ähnlichkeiten und
                                > gruppiert diese zu sogenannten Themen-Clustern. Je mehr Inhalte in
                                > einem Cluster untergebracht werden können, desto wichtiger wird dieses Cluster es und
                                > desto höher ist das Gewicht des Themas, welches durch das Cluster repräsentiert wird. Werden einem Cluster für längere
                                > Zeit nur wenige oder gar keine Daten zugeordnet, verliert das Cluster/Thema an Gewicht und
                                > damit an Bedeutung, bis es vielleicht sogar aus der hier angezeigten Darstellung wieder verschwindet.
                                > Können Daten (weil sie nicht zu bisherigen Inhalten passen) keinem Cluster/Thema zugeordnet werden, entsteht ein neues Cluster, das
                                > über die Zeit an Bedeutung gewinnen oder auch wieder verschwinden kann.

                                *Darstellung im Dashboard - Was man sieht:*

                                > In unserem Dashboard wird die Entwicklung von Themen-Clustern als
                                > Zeitreihe von deren Gewichten dargestellt. Dies ermöglicht
                                > menschlichen Beobachtern zuallererst eine Beurteilung der
                                > Themenentwicklung über längere Zeit und natürlich auch die Entdeckung
                                > von Auffälligkeiten. So kann etwa ein starker und kurzfristiger
                                > Anstieg der Wichtigkeit eines Themas auf ein besonderes Ereignis aber
                                > auch auf koordinierte (vielleicht sogar automatisierte) Aktivität hinweisen.
                                > Das Dashboard zeigt fortlaufend die Entwicklung der Themen-Cluster über ein Zeitfenster von 5 Stunden an.

                                Um diese Beobachtungen genauer untersuchen zu können, stehen Nutzerinnen und Nutzern eine Menge von Detailansichten auf jedes relevante Thema zur Verfügung. Um diese Detaildaten abzurufen klicken Sie in der Zeitreihe auf die (bunte) Kurve eines Themas (Cluster) zu einem gewünschten Zeitpunkt.

                                Die angezeigten Detailinformationen ermöglichen eine genauere Analyse: Es finden sich z.B. Informationen zu Inhalten der Themen-Cluster, Statistiken zu den Clustern selbst, aber auch Metriken zu den Profilen der beteiligten an dem Thema beteiligten Twitter-Accounts. So kann z.B. untersucht werden, wie viele (oder wie wenige) Accounts an der Entwicklung eines Themas beteiligt sind und ob es verifizierte Accounts sind. Das Alter der Accounts kann einen Hinweis darauf, geben, ob die Accounts speziell für dieses Thema (z.B. zum Antreiben einer Kampagne) angelegt wurden. Die Statistiken über Follower, Likes oder Freundschaften können Indizien für die Vernetzung und damit auch die Authentizität und Koordinierung von Accounts sein.

                            ''')
                        ]),
                        dcc.Tab(label='Wichtiger Hinweis zur Nutzung', children=[
                            dcc.Markdown('''
                                Es ist wichtig darauf hinzuweisen, dass wir mit diesem Dashboard an keiner Stelle einen Indikator als alleiniges Merkmal für die Identifikation einer möglichen (Desinformations-)Kampagne herausheben möchten oder ein Thema per se als Kampagne kennzeichnen wollen. Das Dashboard dient als technische Hilfestellung für die menschliche Beurteilung der Aktivitäten auf Twitter und kann bei der Identifikation koordinierter Aktivitäten unterstützen. Wir haben hier ganz bewusst Inhalte und Account-Daten aggregiert um die persönlichen Daten und Meinungen jede/r Nutzer*in zu schützen. Jeder Verdachtsfall muss im Zweifel intensiv untersucht und auf Relevanz geprüft werden.
                            ''')
                        ]),
                        dcc.Tab(label='Impressum & Datenschutz', children=[
                            dcc.Markdown('''
                                ### Impressum

                                Westfälische Wilhelms-Universität Münster\n
                                Schlossplatz 2, 48149 Münster\n
                                Telefon: +49 251 83-0\n
                                Fax: +49 251 83-32090\n

                                E-Mail: [verwaltung@uni-muenster.de](http://wwwuv2.uni-muenster.de/kommentieren/kontakt.php?empf=verwaltung&k=1)

                                Die Westfälische Wilhelms-Universität (WWU) Münster ist eine Körperschaft des öffentlichen Rechts und zugleich eine Einrichtung des Landes Nordrhein-Westfalen. Sie wird vertreten durch Rektor Prof. Dr. Johannes Wessels.

                                **Zuständige Aufsichtsbehörde**:

                                Ministerium für Kultur und Wissenschaft des Landes Nordrhein-Westfalen\n
                                Völklinger Straße 49\n
                                40221 Düsseldorf.

                                *Umsatzsteuer-ID-Nummer: DE 126118759*\n

                                **Redaktionell verantwortlich gemäß §5 TMG**

                                PD Dr. Christian Grimme\n
                                Westfälische Wilhelms-Universität\n
                                Institut für Wirtschaftsinformatik\n
                                Leonardo-Campus 3, 48149 Münster\n
                                E-Mail: [christian.grimme@uni-muenster.de](mailto:christian.grimme@uni-muenster.de)

                                Dieses Impressum gilt für die Informationsangebote der Westfälischen Wilhelms-Universität auf der Webseite des Dashboards, die über die URL [btw-21.uni-muenster.de](https://btw-21.uni-muenster.de/) erreichbar sind und durch den Vermerk "© Universität Münster" gekennzeichnet sind. Für alle anderen Seiten auf diesem WWW-Server liegt die redaktionelle Verantwortung bei den jeweiligen Stellen oder Personen, die die Seiten erstellt und veröffentlicht haben.\n


                                ### Datenschutz

                                Die Datenschutzregelungenen der Westfälischen Wilhelms-Universität Münster finden sich unter folgendem Link:
                                [Datenschutzhinweis](https://www.uni-muenster.de/de/datenschutzerklaerung.html)\n

                                **Spezielle Regelungen für das Dashboard:**

                                - Das Dashboard zeigt Daten an und sammelt keine persönlichen Daten von NutzerInnen des Dashboards. Ebenso benötigen NutzerInnen des Dashboards keinen Twitter Account oder Zugangsdaten für die Abfrage der Daten.
                                - Das Dashboard zeigt Daten nur in aggregierter Form an. Nutzernamen und vollständige Nachrichten werden nicht angezeigt. Sie werden für die interne Verarbeitung aber über die Twitter API erhoben und gemäß den Richtlinien von Twitter gespeichert.
                                - Daten, die bei einer (freiwilligen) Teilnahme an einer Umfrage zum Dashboard entstehen, werden anonymisiert und ohne Metadaten für die statistische Auswertung und die Aufnahme von Feedback gespeichert.




                            ''')
                        ])
                    ])
                )
            ],style={"border": "0 0 0 0"}
        ),
     id="general-collapse",
    is_open=True
    )

    ],
    style={"border": "0px"}
    )

    return card



def register_callback(app, API_IP, API_PORT):
    @app.callback(
        Output("modal-form", "is_open"),
        Output("modal-filled-out", "is_open"),
        [Input("survey_button","n_clicks"), Input("survey_button2","n_clicks")],
        [State("survey_storage", "data"),State("modal-form", "is_open")],
    )
    def toggle_modal(survey_button,survey_button2,data,is_open):

        URL = "http://{}:{}/checksurvey?user_session={}".format(
             API_IP, API_PORT,data)
        r1 = requests.get(url=URL)
        result = r1.json()
        print(result)
        if survey_button or survey_button2:
            ## open survey if not filled out
            if result == "False":
                return 1, 0
            ## open already filled out
            elif result == "True":
                return 0, 1
        else:
            return 0, 0


    @app.callback(
        Output("general-collapse", "is_open"),
        Output("collapse-button", "children"),
        [Input("collapse-button", "n_clicks")],
        [State("general-collapse", "is_open"),
        State("collapse-button", "children")],
    )
    def toggle_collapse(n, is_open, children):
        if n:
            if is_open:
                return not is_open, [html.Div("Allgemeine Informationen",style={"display": "inline-block", "margin-right":"5px"}), html.Div(className="fa fa-lg fa-angle-up")]
            else:
                return not is_open, [html.Div("Allgemeine Informationen",style={"display": "inline-block", "margin-right":"5px"}), html.Div(className="fa fa-lg fa-angle-down")]
        return is_open, children


    @app.callback(
        Output("modal_body", "children"),
        Output("survey_submit", "style"),
        [Input("survey_submit", "n_clicks")],
        [State("survey_storage", "data"),
         State("modal_body", "children"),
         State("gender", "value"),
         State("age", "value"),
         State("use", "value"),
         State("general-manipulation", "value"),
         State("btw-manipulation", "value"),
         State("more", "value"),
         State("help_detection", "value")],
    )
    def survey_submit(submit, data, modal_body, gender,age,use,general_manipulation,btw_manipulation,more,help_detection):
        if submit:
            URL = "http://{}:{}/submitsurvey".format(
             API_IP, API_PORT)

            dat = {"session":data, "gender":gender, "age":age, "useful":use,"general_manipulation":general_manipulation,"btw_manipulation":btw_manipulation, "more":more, "help_detection":help_detection}
            print(dat)
            res = requests.post(URL, json = dat).json()

            return "Vielen Dank für die Teilnahme!",{'display': 'none'}
        return modal_body, {}
