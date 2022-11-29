for i in {1..5}
do
    for player_one in 'random' 'sequential' 'minimax'
    do
        for player_two in 'random' 'sequential' 'minimax'
        do
            python cli.py --player1 ${player_one} --player2 ${player_two}
        done
    done
done