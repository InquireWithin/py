from droids import *
from array_queue import *
from node_stack import *
def unload_parts(filename, belt):
    with open(filename) as file:
        for part in file:
            part = part.strip()
            belt.enqueue(part)
            #add a part where it checks for a blank line
def install_part(droid, my_belt, their_belt):
    if not my_belt.is_empty():
        part = my_belt.dequeue()
        if droid.is_needed(part):
            droid.install(part)
        else:
            their_belt.enqueue(part)
    return droid.is_complete()

def assemble_droids(worker_belt, coworker_belt):
    #create an empty proto droid and an empty astro droid
    #use a loop and install part func to build one proto droid and one astro droid
    #stop when complete, then print

    #create a cargo ship and an empty shipping container (list, and a stack)


    proto = Droids("1984", PROTOCOL)
    astromech = Droids("2020", ASTROMECH)

    cargo_ship = []
    container = Stack()
    while not worker_belt.is_empty() or not coworker_belt.is_empty():
        install_part(proto, worker_belt, coworker_belt)
        #if droid was completed, pack it into a shipping container
        #if the shipping container is full loadit into the ship and
        #create a new shipping container
        container.push(proto)
        proto = Droids("1984", PROTOCOL)
        if container.size() > 4:
            cargo_ship.append(container)
            container = Stack()
        #build an astromech droid using install_part
        install_part(astromech, coworker_belt, worker_belt)
        #if droid was completed, pack it into a shipping container
        #if the shipping container is full loadit into the ship and
        #create a new shipping container
        container.push(astromech)
        proto = Droids("2020", ASTROMECH)
        if container.size() > 4:
            cargo_ship.append(container)
            container = Stack()
    # if last shipping container is not empty
    if not container.is_empty():
        cargo_ship.append(container)
    return cargo_ship

    #print(repr(proto))
   #print(repr(astromech))
    #print(worker_belt)
    #print(coworker_belt)

def ship(cargo_ship):
    #unpacks cargo ship
    container_number = 1
    for container in cargo_ship:
        container_number +=1
        print("Unpacking container number", container_number)
        while not container.is_empty():
            droid = container.pop()
            print(" ", droid)
def the_main():
    worker_belt = Queue()
    coworker_belt = Queue()
    unload_parts("data/parts_0001_0001.txt", worker_belt)
    assemble_droids(worker_belt, coworker_belt)
    cargo_ship = assemble_droids(worker_belt, coworker_belt)
    ship(cargo_ship)

if __name__ == "__the_main__":
    main()

