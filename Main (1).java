
// Linear hash table structure starts
public class LinearhashTable {
    private String[] hashData;
    private int numItems;
    private int maxItems;
    private double loadFactor;

    public LinearhashTable(int size,double lf){
        hashData = new String[size];
        maxItems=size;
        numItems=0;
        loadFactor=lf;
    }
// Converting into integer - 1st step
    public int hashFunction(String item){
        int value=0,weight=1;
        for (int x = 0 ;x <item.length();x++){
            value+= weight*item.charAt(x);
            weight++;
        }
        return value%maxItems;
    }
    // No collision
    public void add(String word){
        int loc = hashFunction(word);
        hashData [loc] = word;


  // if collision happens while putting number in array
            public void add(String word){
        if (numItems/maxItems < loadFactor){
            int loc = hashFunction(word);
            System.out.println(word+" hashed to "+loc);
            // collision resolution strategy always goes here
            while(hashData[loc]!=null && !hashData[loc].equals("__DELETED__")){
                loc = (loc + 1 )%maxItems;
                /* ALTERNATIVE TO THE LINE ABOVE
                    loc = loc +1 ;
                    if (loc == maxItems)
                        loc=0;*/
            }
            // where is the number added
            hashData[loc]=word;
            System.out.println(word+" was added to "+loc);
            numItems++;
        }
    }

    private int search(String word){
        int loc = hashFunction(word);
        while(hashData[loc]!=null && !hashData[loc].equals(word)){
            loc = (loc + 1 )%maxItems;
        }
        if (hashData[loc]!=null)
            return loc;
        return -1;
    }

    public void delete(String word){
        int loc = hashFunction(word);
        while(hashData[loc]!=null && !hashData[loc].equals(word)){
            loc = (loc + 1 )%maxItems;
        }
        if (hashData[loc]!=null){
            hashData[loc]="__DELETED__";
            numItems--;
        }
    }
    public boolean exists(String word){
        int result = search(word);
        if (result==-1)
            return false;
        return true;
    }

    public String retrieve(String word){
        int result = search(word);
        if (result==-1)
            return null;
        return hashData[result];
    }


    public void printTable(){
        System.out.println("_________  HASH TABLE DATA ________");
        for (int x=0; x<maxItems;x++){
            System.out.println("loc "+x+" -> "+hashData[x]);
        }
        System.out.println("________________________________");
    }


}

    public static void main(String[] args) {
        //LinearhashTable lt = new LinearhashTable(14,0.75);
        //QuadHashTable lt = new QuadHashTable(14,0.75);
        DoubleHashTable lt = new DoubleHashTable(14,0.75);
        lt.add("banana");
        lt.add("apple");
        lt.add("pear");
        lt.add("passionfruit");
        lt.add("orange");
        lt.add("strawberries");
        lt.add("dragonfruit");
        lt.add("blueberries");
        lt.printTable();
        lt.delete("apple");
        lt.printTable();
        System.out.println(lt.exists("apple"));
        System.out.println(lt.exists("blueberries"));
        System.out.println(lt.exists("rhododendron"));
        lt.add("apple");
        lt.printTable();
    }


