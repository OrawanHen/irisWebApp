import psycopg2

def fetch_data_from_database():
    conn = psycopg2.connect(
        dbname='postgres',
        user="postgres",
        password="12345678",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    sql = 'SELECT * FROM public."IRIS_table"'
    cur.execute(sql)
    rows = cur.fetchall()
    alldata = """
        <!DOCTYPE html>
        <html>

        <head>
            <title>IRIS TABLE</title>
            <style>
                table {
                    border-spacing: 1;
                    border-collapse: collapse;
                    background: white;
                    border-radius: 6px;
                    overflow: hidden;
                    max-width: 800px;
                    width: 100%;
                    margin: 0 auto;
                    position: relative;

                    * {
                        position: relative
                    }

                    td,
                    th {
                        padding-left: 8px
                    }

                    thead tr {
                        height: 60px;
                        background: #FFED86;
                        font-size: 16px;
                    }

                    tbody tr {
                        height: 48px;
                        border-bottom: 1px solid #E3F1D5;

                        &:last-child {
                            border: 0;
                        }
                    }

                    td,
                    th {
                        text-align: left;

                        &.l {
                            text-align: right
                        }

                        &.c {
                            text-align: center
                        }

                        &.r {
                            text-align: center
                        }
                    }
                }
            </style>
        </head>

        <body>
            <h2>IRIS TABLE</h2>

            <table>
                <tr>
                    <th>sepal_length</th>
                    <th>sepal_width</th>
                    <th>petal_length</th>
                    <th>petal_width</th>
                    <th>Result</th>
                </tr>
        """

    for row in rows:
        alldata += "<tr>"
        for column in row:
            alldata += f"<td>{column}</td>"
        alldata += "</tr>"

    alldata += """
            </table>
        </body>

        </html>
        """
    cur.close()
    conn.close()
    return alldata
