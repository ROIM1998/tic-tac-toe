

function query_move(row, col) {
    console.log("query_move");
    console.log(row);
    console.log(col);
    $.ajax({
        url: '/tic-tac-toe/move',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify({
            row: row,
            col: col,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        }),
        success: function (data) {
            console.log("success");
            console.log(data);
        },
        error: function (data) {
            console.log("error");
            console.log(data);
        }
    });
}

document.querySelectorAll(".cell").forEach(item => {
    item.addEventListener('click', event => {
        //handle click    
        cell_id = event.target.id;
        console.log(cell_id);
        const re = new RegExp('cell-(\\d+)');
        const match = re.exec(cell_id);
        cell_id_int = parseInt(match[1]);
        row = Math.floor(cell_id_int / 3);
        col = cell_id_int % 3;
        query_move(row, col);
    })
})

