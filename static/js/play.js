var now_char = 'X';

function query_move(row, col, target) {
    console.log("query_move");
    console.log(row);
    console.log(col);
    if (target.querySelector('img').src.includes("X.png") || target.querySelector('img').src.includes("O.png")){
        alert("This cell is already occupied! Try another one.");
        return;
    }
    target.querySelector('img').src = '/static/img/'+ now_char +'.png';
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
            if(data['success']){
                if(data['gameover']){
                    alert("Game Over");
                }else{
                    now_char = now_char == 'X' ? 'O' : 'X';
                    if(data['with_bot']){
                        row = parseInt(data['bot_move'][0]);
                        col = parseInt(data['bot_move'][1]);
                        cell_id = 'cell-' + (row * 3 + col);
                        bot_target = document.getElementById(cell_id);
                        bot_target.querySelector('img').src = '/static/img/'+ now_char +'.png';
                        now_char = now_char == 'X' ? 'O' : 'X';
                    }
                }
            }
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
        query_move(row, col, event.target);
    })
})

