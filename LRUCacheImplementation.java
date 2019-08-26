//LRU cache Java implementation

/*  Theory:

Cache: High speed storage mechanism, from which data can be retrieved efficiently. It's size is fixed, you can insert and search with O(1) complexity (ideally).

LRU Cache: A type of cache where the least recently used entry is removed if the cache is full. It needs to keep track of how much each entry is called.

Implementation Overview: In order to write a cache that keeps track of entry usage and maintains O(1) time for insert and look up, 2 data structures are required. Because hashmaps store key/value pairs, they provide O(1) time for insertion and lookup.
Doubly linked lists also provide O(1) time for insertion and we can implement them in a way that allows us to track how many times entries are accessed. Therefore, the implementation will consist of a hashmap holding keys for the nodes of a doubly linked list.

Implementation Strategy: We define an entry as essentailly a Node object, with a value and a key. When querying an entry, the hashmap get() is used to get the entry using a given key. From there, in order to keep track of the fact that the entry was used, it is removed 
and placed at the top of the doubly linked list. The value of the entry is held and can be retrieved once the tracking is done.

Geo-Distributed: Although I have very little experience with caches, in order to make this cache implementation geo-distributed, I believe you would want to have a docker container system on your servers, where every server would have it's own cache. 
The caches would be synced using kubernetes.
*/

import java.util.HashMap;
import java.util.Scanner;

class Entry{
	//Define the entry as a node (with left and right) but include value and key
    int value;
    int key;
    Entry left;
    Entry right;
}

public class LRUCache {

	HashMap<Integer, Entry> hashmap;
	Entry start, end;
    int LRU_SIZE = 10; //set for example, could be changed
	
	//declare the hashmap object, consisting of Entries with integer keys
	public LRUCache() {
		hashmap = new HashMap<Integer, Entry>();
	}

	public int getEntry(int key) {
		long endTime = System.currentTimeMillis() + 10000;
		while(true){
		//if entry already exists
		if (hashmap.containsKey(key))
		{
			Entry entry = hashmap.get(key);
			/*because it is being used, it is taken from the end of the list and put first, it is now the most
			recently used entry.*/
			removeNode(entry);
			addAtTop(entry);
			return entry.value; //return value of entry you are querying
		}
		//fail if entry does not exist
		return -1;
		//check if operation is taking too long
		if (System.currentTimeMillis() > endTime) {
            System.out.println("ERROR: timeout");
            return;
        }
		}
		

	}

	public void putEntry(int key, int value) {
		long endTime = System.currentTimeMillis() + 10000;
		while(true){
		//if entry already exists
		if (hashmap.containsKey(key)) //if entry exists, do not remake, update
		{
			Entry entry = hashmap.get(key);
			entry.value = value;
			removeNode(entry);
			addAtTop(entry);
		} else {
			//new Entry object
			Entry newnode = new Entry();
			newnode.left = null;
			newnode.right = null;
			//set key and value
			newnode.value = value;
			newnode.key = key;
			if (hashmap.size() > LRU_SIZE) // We have reached maxium size so need to make room for new element.
			{
				//removes least recently used entry
				hashmap.remove(end.key);
				removeNode(end);				
				addAtTop(newnode);

			} else {
				addAtTop(newnode);
			}

			hashmap.put(key, newnode);
		}
		//check if operation is taking too long
		if (System.currentTimeMillis() > endTime) {
            System.out.println("ERROR: timeout");
            return;
        }
		}
	}

	//adds entry at the front of the doubly linked list
	public void addAtTop(Entry node) {
		node.right = start;
		node.left = null;
		if (start != null)
			start.left = node;
		start = node;
		if (end == null)
			end = start;
	}

	//removes entry
	public void removeNode(Entry node) {

		if (node.left != null) {
			node.left.right = node.right;
		} else {
			start = node.right;
		}

		if (node.right != null) {
			node.right.left = node.left;
		} else {
			end = node.left;
		}
	}

}