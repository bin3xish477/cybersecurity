import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.Serial;
import java.io.Serializable;
import java.lang.reflect.Method;

public class BadThing implements Serializable {
    // this loosely defined object allows for the insecure deserialization opportunity
    // since we can define our own malicious class which would a valid `Object`
    Object ldt;
    String methodName;

    @Serial
    private void readObject(ObjectInputStream ois) throws ClassNotFoundException, IOException {
        ois.defaultReadObject();
        try {
            Method method = ldt.getClass().getMethod(methodName);
            method.invoke(ldt);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
