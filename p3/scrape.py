# project: p3
# submitter: hbian8
# partner: none
# hours: 10
import os, sys, importlib, json, re
from subprocess import Popen
import traceback
from collections import deque
import pandas as pd
import time
import requests

class Parent:
    def twice(self):
        self.message()
        self.message()

    def message(self):
        print("parent says hi")


class Child(Parent):
    def message(self):
        print("child says hi")


class GraphSearcher:
    def __init__(self):
        self.visited = set()
        self.order = []

    def go(self, node):
        raise Exception("must be overridden in sub classes -- don't change me here!")

    def dfs_search(self, node):
        # 1. clear out visited set
        self.visited.clear()
        self.order.clear()
        # 2. start recursive search by calling dfs_visit
        self.dfs_visit(node)

    def dfs_visit(self, node):
        # 1. if this node has already been visited, just `return` (no value necessary)
        if node in self.visited:
            return
        # 2. mark node as visited by adding it to the set
        self.visited.add(node)
        # 3. add this node to the end of self.order
        self.order.append(node)
        # 4. get list of node's children with this: self.go(node)
        children = self.go(node)
        # 5. in a loop, call dfs_visit on each of the children
        for child in children:
            self.dfs_visit(child)

    def bfs_search(self, node):
        self.visited.clear()
        self.order.clear()
        self.bfs_visit(node)

    def bfs_search(self, node):
        q = deque()
        q.append(node)
        while len(q) > 0:
            cur_node = q.popleft()
            self.order.append(cur_node)
            children = self.go(cur_node)
            for child in children:
                if child not in self.order and child not in q:
                    q.append(child)


class MatrixSearcher(GraphSearcher):
    def __init__(self, df):
        super().__init__()  # call constructor method of parent class
        self.df = df

    def go(self, node):
        children = []
        # TODO: use `self.df` to determine what children the node has and append them
        for nd, has_edge in self.df.loc[node].items():
            if has_edge == 1:
                children.append(nd)
        return children


class FileSearcher(GraphSearcher):
    def __init__(self):
        super().__init__()
        self.msg = str()

    def go(self, node):
        with open(os.path.join("file_nodes", node), "r") as f:
            data = f.read().splitlines()
        value = data[0]
        self.msg += value
        children = str(data[1]).split(",")
        return children

    def message(self):
        return self.msg


class WebSearcher(GraphSearcher):
    def __init__(self, web_driver):
        super().__init__()
        self.webdriver = web_driver

    def go(self, node):
        children = []
        self.webdriver.get(node)
        urls = self.webdriver.find_elements(by="tag name", value='a')
        for url in urls:
            children.append(url.get_attribute('href'))
        return children

    def table(self):
        table = pd.DataFrame()
        for url in self.order:
            df_list = pd.read_html(url, match="clue")
            df = pd.concat(df_list, ignore_index=True)
            table = pd.concat([table, df], ignore_index=True)
        return table

def reveal_secrets(driver, url, travellog):
    password = 0
    for num in travellog['clue']:
        password = password * 10 + num
    driver.get(url)
    blank = driver.find_element(by='id', value='password')
    blank.send_keys(password)
    button = driver.find_element(by='id', value='attempt-button')
    button.click()
    time.sleep(1)
    button2 = driver.find_element(by='id', value='securityBtn')
    button2.click()
    time.sleep(1)
    location = driver.find_element(by='id', value='location')
    img = driver.find_element(by='id', value='image')
    src = img.get_attribute('src')
    r = requests.get(src, allow_redirects=True)
    open('Current_Location.jpg', 'wb').write(r.content)
    return location.text

df = pd.DataFrame([
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
], index=["A", "B", "C", "D"], columns=["A", "B", "C", "D"])

m = MatrixSearcher(df)
m.bfs_search("B")
print(m.order)
m.order