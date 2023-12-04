#           Вариант 1
# def hanoi(n, source, auxiliary, destination):
#     if n > 0:
#         hanoi(n-1, source, destination, auxiliary)
#         print(f'Disc {n} move from {source} to {destination}')
#         hanoi(n-1, auxiliary, source, destination)

# hanoi(3, 'A', 'B', 'C')

#           Вариант 2

class TowerOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.tower_a = list(range(num_disks, 0, -1))
        self.tower_b = []
        self.tower_c = []

    def move_disk(self, source, destination):
        disk = source['tower'][-1]
        source['tower'] = source['tower'][:-1]
        destination['tower'].append(disk)
        print(f"Move disk {disk} from Tower {source['name']} to Tower {destination['name']}")

    def hanoi_recursive(self, num_disks, source, destination, auxiliary):
        if num_disks == 1:
            self.move_disk(source, destination)
        else:
            self.hanoi_recursive(num_disks - 1, source, auxiliary, destination)
            self.move_disk(source, destination)
            self.hanoi_recursive(num_disks - 1, auxiliary, destination, source)

    def solve(self):
        source = {'tower': self.tower_a, 'name': 'A'}
        auxiliary = {'tower': self.tower_b, 'name': 'B'}
        destination = {'tower': self.tower_c, 'name': 'C'}

        self.hanoi_recursive(self.num_disks, source, destination, auxiliary)


num_disks = 3
hanoi_tower = TowerOfHanoi(num_disks)
hanoi_tower.solve()
