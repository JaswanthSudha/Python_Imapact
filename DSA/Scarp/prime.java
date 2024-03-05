import java.lang.*;
class first
{
    private String brand;
     private int price;
     private String name;
     static
     {
         System.out.println("in static block");
     }
    public void show()
    {
        System.out.println(brand+":"+price+":"+name);
    }
}
class second
{
    public static void main(String args[])
    {
        first obj1=new first();
        //obj1.show();
        obj1.show(1500);
        obj1.show("phone");
        first obj2=new first();
        //obj2.show();
        obj2.show(1700);
        obj2.show("sphone");
    }
}