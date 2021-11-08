import dash_core_components as dcc
import dash_table


def assignment_tab_layout():
    return dcc.Tab(label='Assignment', children=[
        dash_table.DataTable(
            id='textTable',
            columns=[
                {
                    "name": "Profilbild",
                    "id": "profilePicture",
                    "presentation": "markdown"
                },
                {
                    "name": "Inhalt",
                    "id": "text",
                    "presentation": "markdown"
                },
                {
                    "name": "Zeitstempel",
                    "id": "time"
                }
            ],
            style_cell={
                'textAlign': 'left',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'whiteSpace': 'normal',
            },
            style_table={'maxWidth': "100%",
                         "table-layout": "fiexed"},
            style_header={
                "color": "black"
            },
            style_cell_conditional=[
                {'if': {'column_id': "text_id"},
                    'width': '90px'},
                {'if': {'column_id': "time"}, 'width': '120px'}
            ],
            page_action="native",
            page_current=0,
            page_size=8,
            sort_action="native",
            filter_action="native"
        )
    ])
