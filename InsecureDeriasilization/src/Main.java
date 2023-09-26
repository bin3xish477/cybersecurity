import java.lang.reflect.Method;

public class Main {
    public static void main(String[] args) {
        BadThing badThing = new BadThing();
        badThing.ldt = new CustomObj();
        badThing.methodName = "payload";

        try {
            Method method = badThing.ldt.getClass().getMethod(badThing.methodName);
            method.invoke(null);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}