//单一用户登录
import java.util.Scanner;
public class supermarket{
    private static GoodsName[]Goods=new GoodsName[4];
    static CustomerManager userManager=new CustomerManager();
    static{
        Goods[0]=new GoodsName("缤纷多味糖果",3.0,100);
        Goods[1]=new GoodsName("五彩纸屑气球",1.5,50);
        Goods[2]=new GoodsName("亲子装斗篷",35,100);
        Goods[3]=new GoodsName("晨光中性笔",1.5,250);
    }
    public static void main(String[] args){
        Scanner input=new Scanner(System.in);
        boolean isregister=false;
        User user=new User();     //多用户      //User2 user=new User2();
        while(true) {
            System.out.println("************欢迎来到理工超市管理系统************");
            System.out.println("***1.用户注册 2.用户登录 3.浏览商品 4.查看商品***");
            System.out.println("***5.加入购物车 6.查看购物车 7.结算 0.退出系统***");
            System.out.println("********************************************");
            int choice = input.nextInt();
            switch (choice) {
                case 1:
                    if (user.register() == 1)
                        isregister = true;
                    break;
                case 2:
                    if (!isregister)
                        System.out.println("您尚未注册账号，请先注册。");
                    else {
                        System.out.println("正在登录中:");
                        user.login();
                    }
                    break;
                case 3:
                    System.out.println("编号" + "\t\t" + "商品名称" + "\t\t" + "单价" + "\t\t" + "数量");
                    for (int i = 0; i < 4; i++)
                        System.out.println(i + 1 + "\t" +Goods[i].getName()+"\t\t"+Goods[i].getPrice()+"    "+Goods[i].getCount());
                        break;
                case 4:
                    System.out.println("正在查看商品，请输入需要查看的商品的编号：");
                    int Choice = input.nextInt();
                    while (true) {
                        int k;
                        if (Choice >= 1 && Choice <= 4) {
                            System.out.println("编号" + "   " + "商品名称" + "   " + "单价" + "  " + "数量");
                            System.out.println(Choice + "\t" + Goods[Choice - 1].getName()+ "\t" + Goods[Choice-1].getPrice()
                                    + "   " + Goods[Choice - 1].getCount());
                            System.out.println("是否继续查看商品？1-YES 2-NO");
                            k = input.nextInt();
                            if (k == 1) {
                                System.out.println("请输入商品编号：");
                                Choice = input.nextInt();
                            } else {
                                System.out.println("欢迎下次光临！");
                                break;
                           }
                        } else {
                            System.out.println("抱歉您所查看的商品不存在。");
                            System.out.println("是否继续查看其它商品？1-YES 2-NO");
                            k = input.nextInt();
                            if (k == 1) {
                                System.out.println("请输入商品编号：");
                                Choice = input.nextInt();
                            } else
                                System.out.println("欢迎下次光临！");
                        }
                    }
                    break;
                case 5:
                    break;
                case 6:
                    break;
                case 7:
                    break;
                case 0:
                    System.out.println("欢迎下次光临！");
                    return;
            }
        }
    }
}
