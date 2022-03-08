import java.util.Scanner;
public class User2 {
    private String name = "";
    private String passward = "";

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPassward() {
        return passward;
    }

    public void setPassward(String passward) {
        this.passward = passward;
    }

    public void login() {
        System.out.println("输入用户名：");
        Scanner scanner = new Scanner(System.in);
        String username = scanner.next();
        System.out.println("输入密码：");
        String passward = scanner.next();
        if (this.name.equals(username) && this.passward.equals(passward));
        System.out.println("登录成功！");
    }
    public int register() {
        int m = 0;
        int random=(int)(Math.random()*9000)+1000;
        Scanner input=new Scanner(System.in);
        System.out.println("正在进行用户注册，请输入下列信息。");
        System.out.println("请输入用户名：");
        this.name = input.next();
        System.out.println("请输入密码：");
        this.passward=input.next();
        System.out.println("请再次输入密码：");
        String pwd2=input.next();
        while(!pwd2.equals(this.passward)){
            System.out.println("对不起，密码不一致，请再次输入密码：");
            pwd2=input.next();
        }
        System.out.println("请输入验证码：" + random);
        int number = input.nextInt();
        if (number != random)
            System.out.println("验证码错误，请再次输入。");
        else {
            System.out.println("恭喜您注册成功！");
            Customer cus=new Customer(this.name,this.passward);
            m++;
        }
        return m;
    }
}
