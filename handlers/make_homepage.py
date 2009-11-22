def create_file_name( file_name, file_id ):
    print """<div id='mainheader'>
             <h2>
             <a href='index.py?
             file_id=""", file_id, ">", title_clear,
             """</a>
             </h2>
             </div>
            """

def get_raw_data( file_id ) {
        con1 = connect("host=localhost port=5432 dbname=noaa user=noaa password=123");
        # to get fileName and fileID
        result = con1.query( 
            'SELECT file_name, file_id
            FROM files f
            LEFT JOIN courses c ON f.file_id = c.file_id
            WHERE file_id = $1',
            array( file_id ) 
            );
        return $result;
