l = [
        ['Paris', 'London', 'New York'],
        [45, True, 5.5, 'hello'],
        -3,
        [
            5,
            [
                '#',
                '$',
                '%',
                '^',
                [10, 20, 30, 40]
            ]
        ],
        [
            ['a'],
            ['b'],
            'c',
            [
                ['d']
            ]
        ]
]


print(l[2])
print(l[1][2])
print(l[0][-1::-1])
print(l[1:3])
print(l[3][1][3])
print(l[4][0][0])
print(l[4][1])
print(l[4][3][0][0])
print(l[3][1][4][1::2])
print(l[3][1][-2::-3])