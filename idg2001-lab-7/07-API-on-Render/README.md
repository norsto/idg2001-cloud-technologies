# APIs on Render
We want two APIs on Render:
- Main node: Has a data structure which you can read, write and delete from.
- Passthrough node: Passes messages through to the main node, and returns to sender.


Main node has the data structure ("database" from wish). When adding a thing to the main node, it'll update its "database". When adding a thing to the passthrough node, it'll forward the post to the main node, and update the user/client.


Example pseudo-ish-code for main node
```python
def main_node_get(...):
    ...
    return <some data>
```


Example pseudo-ish-code for passthrough node
```python
def passthrough_node_get(...):
    <send get to main node>
    data = ...
    return data
```
