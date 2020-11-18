package fibo_series;
import java.util.Scanner ;
import java.math.BigInteger;
import java.lang.Math ;

public class Fibonacci {
   private int n, curr_col = 0; //row = 0 ;
   private boolean Ready = false ;
   private static Scanner Sc = new Scanner(System.in);
   
   private int Num_Width(BigInteger n)
   { StringBuffer Number = new StringBuffer() ;
      Number.append(n) ;
      return Number.length();
   }
   
   private String No_Show(BigInteger n, long w)
   {  StringBuffer Print = new StringBuffer() ;
      StringBuffer Number = new StringBuffer();
     
     Number.append(n) ;
     if(w <= Number.length()) return String.format(" %d", n) ;
     
     for(int i=0; i<w-Number.length(); i++)
    	Print.append(" ") ;
      Print.append(Number) ;
     return Print.toString(); 
   }
   
   private void Reset(boolean NewL) { if(NewL) System.out.print("\n\n  "); curr_col = 0; /*row = 0; */ }
   private void Reset() { Reset(true) ; }
   
   private String Hell()
   { StringBuffer A = new StringBuffer() ; int i ;
     String[] Dict = {"'Difficult'", ", 'Insane'", ", 'Draculous'", ", 'Unrealistic'"} ; // n = 60, 625, 15625, 390625
      if(n < 150) return "" ;
      if(n >= 300) Dict[0] = "'Hell'" ;
      
      for(i=1; Math.pow(30, i) <= n; i++) 
    	 try {A.append(Dict[i-1]) ; }
         catch(ArrayIndexOutOfBoundsException e) { return A.toString(); }
     
      A.append(" ") ; 
     return A.toString();
      // Warning.. Draculous Requirements, may take Hours to meet... ...
      //              Also, it is better to, not think about Unrealistic Ones..
   }
   
   @SuppressWarnings("unused")
   public boolean Input(boolean Print)
   { System.out.print("\n  Enter No. of Elements to be Displayed from the Fibonacci Series  : ");
     String Buffer = Sc.nextLine();
     try { n = Integer.parseInt(Buffer); }
     catch(NumberFormatException e) 
     { int Trial, i ;
        try 
        { for(i=5; i < Buffer.length(); i+=5)
        	Trial = Integer.parseInt(Buffer.substring(i-5, i)) ;
            Trial = Integer.parseInt(Buffer.substring(i-5)) ;
           System.out.println("   The Number Entered is too Big.. Please, Try Again...");
        }
        catch(NumberFormatException e1) { System.out.println("   This is not a Number... Please Try Again!"); }
       Ready = false ; return Ready ;
     }
     
     Ready = true ;
     if(Print) Output() ;
     return Ready ;
   }
   public boolean Input(int n, boolean Print) { this.n = n ; if(Print) Output() ; return true ;}
   public boolean Input() { return Input(true) ; }
   public boolean Input(int n) { return Input(n, true) ; }
   
   public void Output()
   { //long a = -1, b = 1, c;
     BigInteger a = new BigInteger("-1"), b = new BigInteger("1"), c = new BigInteger("0") ;  
     int max_col=0, width=0 ;
     
     if(Ready == false) { System.out.print("\n No Number to Print upto... ! Sorry... "); return ; }
     System.out.print("\n  ");
     
      for(int i=0; i<n; i++)
      { c = a.add(b) ;
        a = b ;
        b = c ;
        
        curr_col++ ;
        
             if(Num_Width(c) < 5)  { if(width != 8) Reset(false); width = 8; max_col = 15; }
        else if(Num_Width(c) < 8)  { if(width != 10) Reset();  width = 10;   max_col = 12; }
        else if(Num_Width(c) < 13) { if(width != 15) Reset();  width = 15;   max_col = 8 ; }
        else if(Num_Width(c) < 17) { if(width != 20) Reset();  width = 20;   max_col = 6 ; }
        else if(Num_Width(c) < 21) { if(width != 24) Reset();  width = 24;   max_col = 5 ; }
        else if(Num_Width(c) < 27) { if(width != 30) Reset();  width = 30;   max_col = 4 ; }             
        else if(Num_Width(c) < 37) { if(width != 40) Reset();  width = 40;   max_col = 3 ; }
        else if(Num_Width(c) < 57) { if(width != 60) Reset();  width = 60;   max_col = 2 ; }
        else     
          for(int k=60; true; k+=5)
            if(Num_Width(c) < k-3) { if(width != k)  Reset();  width = k ;   max_col = 1 ; break; }
        
        if(curr_col%max_col == 0 && curr_col != 0) 
        {  System.out.print("\n  "); //row++ ;
          //if(max_col == 1 && row%5 == 0) System.out.print("     - \n  ");
        }
        
        System.out.format("%s", No_Show(c, width));
      }
     System.out.format("\n\n  As Per %sRequirements, Fibonacci Series has been Printed !!", Hell()) ; 
   }
   
  public static void main(String[] args)
  { System.out.print("\n  Here, we are going to Print Out, Fibonacci Series upto 'n' Terms ");

     Fibonacci F = new Fibonacci() ;
      while(!F.Input()) ;
    
  }
}
