public class Hello{
	String name="chinnu";
	public void function(){
		String name="JyothiBhaiPule";
		System.out.println(name);
		System.out.println(this.name);
	}
	public static void main(String args[]){
		Hello obj=new Hello();
		obj.function();
	}
}