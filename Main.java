public static int factorial(int n){
        if (n==0) return 1;
        if (n==1) return 1;
        return n *factorial (n-1);
        }
public static int triangular(int n){
        if (n==1) return 1;
        return n + triangular(n-1);
        }

public static void printRecursive(int n){
        if (n > 0 ){
        printRecursive(n-1);
        System.out.print(n+" ");
        }
        }

public static long fibonacci (int n){
        if (n==0) return 0;
        if (n==1) return 1;
        return fibonacci(n-1)+ fibonacci(n-2);
        }

public static long[] memoized;

public static long efficientFibonacci (int n){
        if (n==0) return 0;
        if (n==1) return 1;
        if (memoized[n]!=0) return memoized[n]; // return the answer if it was calculated already

        memoized[n]= efficientFibonacci(n-1)+ efficientFibonacci(n-2);
        return memoized[n];
        }

public static long bestFib(int n){
        long prev1=1,prev2=0,answer=0;
        if (n==0) return 0;
        if (n==1) return 1;
        for (int x=2;x<=n;x++){
        answer =prev1+prev2;
        prev2=prev1;
        prev1=answer;
        }
        return answer;
        }

public static void printStars(int n)  {

        if (n>0){
        for (int x=0;x<n;x++){
        System.out.print("*");;
        }
        System.out.println("");
        printStars(n-1);
        }

        }

public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter a positive integer: ");
        int userVal =sc.nextInt();
        memoized = new long[userVal+1];
        System.out.println("Factorial ("+userVal+") = "+factorial(userVal));
        System.out.println("Triangular ("+userVal+") = "+ triangular(userVal));
        printRecursive(10);
        System.out.println("Memoized Fibonacci ("+userVal+") = "+ efficientFibonacci(userVal));
        System.out.println("Iterative Fibonacci ("+userVal+") = "+ bestFib(userVal));
        System.out.println("Fibonacci ("+userVal+") = "+ fibonacci(userVal));
        printStars(4);
        }
