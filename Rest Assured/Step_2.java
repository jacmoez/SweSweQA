import io.restassured.response.Response;
import org.junit.jupiter.api.MethodOrderer;
import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestMethodOrder;

import java.util.List;
import java.util.Map;
import java.util.Objects;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class Step_2 {

    @Test
    @Order(1)
    public void testListSize(){
        given()
                .when()
                .get("https://jsonplaceholder.typicode.com/posts")
                .then()
                .assertThat()
                .body("$", hasSize(100));

        System.out.println("Test 1 : Check Response Total 100");
    }

    @Test
    @Order(2)
    public void testListContainsItem(){
        given()
                .when()
                .get("https://jsonplaceholder.typicode.com/posts")
                .then()
                .assertThat()
                .body("title", hasItem(startsWith("qui est esse")));
                System.out.println("Test 2 : Success");
    }
    @Test
    @Order(3)
    public void testListContainsItems(){
        given()
                .when()
                .get("https://jsonplaceholder.typicode.com/posts")
                .then()
                .assertThat()
                .body("id", hasItems(1,2,3));
        System.out.println("Test 3 : Success");
    }

    @Test
    @Order(4)
    public  void testExtraList(){
       Response response =  given()
               .when()
               .get("https://jsonplaceholder.typicode.com/posts");

        List<Integer> ids = response.jsonPath().getList("id");

        System.out.println("Extra IDs: " + ids);

        System.out.println("Test 4: Success");
    }

    @Test
    @Order(5)
    public void testJson(){
        Response response = given()
                .when()
                .get("https://jsonplaceholder.typicode.com/posts");

        List<Map <String, Objects >> posts = response.jsonPath().getList("");
//        System.out.println(posts.get(0));

        for(Map<String, Objects> post : posts){
            System.out.println(post);
        }

        System.out.println("Test 5 : JSON Output Success.");
    }


    @Test
    @Order(6)
    public void testListFilter(){
        given()
                .when()
                .get("https://jsonplaceholder.typicode.com/posts")
                .then()
                .assertThat()
                .body("findAll { post -> post.userId == 1}", hasSize(10) );
        System.out.println("Test 6 : List Filter Success");
    }
}
