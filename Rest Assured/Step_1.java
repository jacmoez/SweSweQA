import io.restassured.RestAssured;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class Step_1 {

    @BeforeAll
    public static void setup(){
      RestAssured.baseURI = "https://jsonplaceholder.typicode.com/";
    }

    @Test
    @Order(1)
     void testGetAllPost() {
        given().when().get("/posts").then().statusCode(200).body("$.size()", greaterThan(0));
    }
    @Test
    @Order(2)
    public void testGetPostById(){
        given()
                .pathParams("id",1)
                .when().get("/posts/{id}")
                .then().statusCode(200)
                .body("id", equalTo(1));
    }
    @Test
    @Order(3)
    public void testCreatePost() {
        given()
                .contentType("application/json")
                .body("{ \"title\":  \"New Post\", \"content\":  \"This is a test post\"}")
                .when()
                .post("/posts")
                .then()
                .statusCode(201)
                .body("title", equalTo("New Post"));
    }
    @Test
     @Order(4)
       public void testDeletePost() {
        given()
                .pathParams("id", 1)
                .when()
                .delete("/posts/{id}")
                .then()
                .statusCode(anyOf(is(200), is(202), is(204), is(404)));
       }
       @Test
       @Order(5)
       public void testUpdatePost(){
        given()
                .contentType("application/json")
                .pathParams("id", 1)
                .body("{\"title\":  \"Update Post\", \"content\":  \"Update content\"}")
                .when()
                .put("/posts/{id}")
                .then()
                .statusCode(200)
                .body("title", equalTo("Update Post"));
       }
    @Test
    @Order(6)
    public void testCommentsForPost(){
        given()
                .when()
                .get("/posts/1/comments")
                .then()
                .statusCode(200)
                .body("$.size()", greaterThan(0));
    }
    @Test
    @Order(7)
    public void testGetCommentsPostsIdQueryParam(){
        given()
                .queryParam("postId", 1)
                .when()
                .get("/comments")
                .then()
                .statusCode(200)
                .body("[0].postId", equalTo(1));
    }
}
