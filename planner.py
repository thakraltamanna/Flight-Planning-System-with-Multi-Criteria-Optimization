from flight import Flight
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)
        root = self.heap.pop()
        self._heapify_down(0)
        return root

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        return self.heap[0] if not self.is_empty() else None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self._compare(self.heap[index], self.heap[parent_index]):
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self._compare(self.heap[left_child_index], self.heap[smallest]):
            smallest = left_child_index
        if right_child_index < len(self.heap) and self._compare(self.heap[right_child_index], self.heap[smallest]):
            smallest = right_child_index
        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _compare(self, a, b):
        if a[0] < b[0]: 
            return True
        elif a[0] > b[0]:
            return False
        else: 
            return a[1] <= b[1]



class Planner:
    def __init__(self, flights):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        ##finding number of cities taki i can initialise adj list
        self.flights=flights
        max_city=-1
        for flight in flights:
            city=max(flight.start_city, flight.end_city)
            if max_city<city:
                max_city=city
        no_of_cities=max_city+1

        ##now i will initialize adjaceny list
        self.adj_list=[[] for _ in range(no_of_cities)]

        ##now building the adjacenylist
        for flight in flights:
            index=flight.start_city
            self.adj_list[index].append(flight)

        pass
  
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        pq=MinHeap()
        ##pushing current no of flights taken, current arrival time, curreny city, abhi tak ka route
        pq.push((0,t1,start_city,[]))
        while pq.is_empty() is False:
            node=pq.pop()
            flights_taken=node[0]
            arrival_time=node[1]
            curr_city=node[2]
            route=node[3]
            if curr_city == end_city:
                return route
            
            for possible_route in self.adj_list[curr_city]:
                if (possible_route.departure_time>= arrival_time+20 or arrival_time==t1)  and  possible_route.arrival_time<=t2  and possible_route.end_city != start_city:
                    pq.push((flights_taken +1, possible_route.arrival_time, possible_route.end_city, route + [possible_route]))
        return []  

    
    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        pq=MinHeap()
        ##pushing current no of fare, current arrival time, curreny city, abhi tak ka route
        pq.push((0,t1,start_city,[]))
        while pq.is_empty() is False:
            node=pq.pop()
            fare=node[0]
            arrival_time=node[1]
            curr_city=node[2]
            route=node[3]
            if curr_city == end_city:
                return route
            
            for possible_route in self.adj_list[curr_city]:
                if (possible_route.departure_time>= arrival_time+20 or arrival_time==t1)  and  possible_route.arrival_time<=t2  and possible_route.end_city != start_city:
                    pq.push((fare + possible_route.fare, possible_route.arrival_time, possible_route.end_city, route + [possible_route]))
        return []
    
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        pq=MinHeap()
        ##pushing  no. of flights taken, current no of fare, current arrival time, curreny city, abhi tak ka route
        pq.push((0,0,t1,start_city,[]))
        while pq.is_empty() is False:
            node=pq.pop()
            fare=node[1]
            flights_taken=node[0]
            arrival_time=node[2]
            curr_city=node[3]
            route=node[4]
            if curr_city == end_city:
                return route
            
            for possible_route in self.adj_list[curr_city]:
                if (possible_route.departure_time>= arrival_time+20 or arrival_time==t1)  and  possible_route.arrival_time<=t2  and possible_route.end_city != start_city:
                    pq.push(( flights_taken+1,fare + possible_route.fare , possible_route.arrival_time, possible_route.end_city, route + [possible_route]))
        return []
        