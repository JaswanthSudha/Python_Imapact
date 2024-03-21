import java.util.*;
public class bfs{
    public static void bfs(Queue queue){
        int length=queue.length();
        System.out.println(length);
    }
    public static void main(String args[]){
        Queue<Integer> queue = new PriorityQueue<Integer> (); 
        queue.add(1);
        queue.add(2);
        queue.add(4);
        bfs();

    

    }
}