class Solution{
    static int solve(int[] val,int W,int [] wt,int N,int i){
       if(i==N)
           return 0;

       int include=0;
       if(val[i]<=sum)
        include=val[i]+solve(val,W,wt,N,i+1);
       int exclude=solve(val,W,wt,N,i+1);
       return Math.min(include,exclude);

    }
    public int knapSack(){
        Scanner sc= new Scanner(System.in);
        int N= sc.nextInt();
        int W= sc.nextInt();
        int[] val=new int[N];
        int[] wt=new int[N];
        for(int i=0;i<N;i++){
            val[i]=sc.nextInt();
        }
        for(int i=0;i<N;i++){
            wt[i]=sc.nextInt();
        }
        int sum=0;
        for(int i=0;i<N;i++){
            sum+=val[i];
        }
        int ans=Integer.MAX_VALUE;
        ans=solve(val,W,wt,N,0);
        if(ans<=W){
            return 1;
        }
        return 0;
    }
}