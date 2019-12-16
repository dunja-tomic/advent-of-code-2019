class Node:
    def __init__(self, val):
        self.val = val
        self.root = True
        self.children = []

def build_orbit_graph(arr):
    orbit_graph = {}
    for orbit in arr:
        left = orbit[0]
        right = orbit[1]
        if left not in orbit_graph:
            orbit_graph[left] = Node(left)
        if right not in orbit_graph:
            orbit_graph[right] = Node(right)
        orbit_graph[right].root = False
        orbit_graph[left].children.append(orbit_graph[right])
        orbit_graph[right].children.append(orbit_graph[left])
    return orbit_graph

def part1():
    filepath = "day6.in"
    with open(filepath) as fp:
        arr = fp.readlines()
        arr = [x.strip().split(')') for x in arr]

        seen = set()
        def count_orbits(orbit_graph, root, count=0):
            if root.val in seen:
                return 0
            
            seen.add(root.val)

            if len(root.children) == 0:
                return count

            # for child in root.children:
            return count + sum(count_orbits(orbit_graph, child, count + 1) for child in root.children)

        orbit_graph = build_orbit_graph(arr)
        num_orbits = count_orbits(orbit_graph, orbit_graph['COM'])
        print("The total number of orbits is: " + str(num_orbits))

def part2():
    filepath = "day6.in"
    with open(filepath) as fp:
        arr = fp.readlines()
        arr = [x.strip().split(')') for x in arr]

        orbit_graph = build_orbit_graph(arr)
        you_path = []
        santa_path = []

        seen = set()
        def findPath(orbit_graph, root, path, goal):
            if root.val not in seen:
                seen.add(root.val)
                path.append(root.val)

                if root.val == goal:
                    return True

                for child in root.children:
                    if findPath(orbit_graph, child, path, goal):
                        return True
                
                # Node isn't in the path, so pop it from the path
                path.pop()

        findPath(orbit_graph, orbit_graph['COM'], santa_path, 'SAN')
        seen = set()

        findPath(orbit_graph, orbit_graph['COM'], you_path, 'YOU')

        both = [node for node in you_path if node in santa_path]
        common_ancestor = both.pop()

        num_transfers = len(you_path) - you_path.index(common_ancestor) - 2 + len(santa_path) - santa_path.index(common_ancestor) - 2
        print("The minimum number of transfers is: " + str(num_transfers))

if __name__ == '__main__':
    part1()
    part2()