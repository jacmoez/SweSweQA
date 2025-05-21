//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

import io.restassured.RestAssured;
import io.restassured.response.Response;
import io.restassured.response.ValidatableResponse;
import org.hamcrest.Matchers;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.Test;

public class Step_1 {

    @BeforeAll
    public static void setup() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com/";
    }

    @Test
    @Order(1)
    void testGetAllPost() {
        ((ValidatableResponse)((ValidatableResponse)((Response)RestAssured.given().when().get("/posts", new Object[0])).then()).statusCode(200)).body("$.size()", Matchers.greaterThan(0), new Object[0]);
    }
    @Test
    @Order(2)
    public void testGetPostById() {
        ((ValidatableResponse)((ValidatableResponse)((Response)RestAssured.given().pathParams("id", 1, new Object[0]).when().get("/posts/{id}", new Object[0])).then()).statusCode(200)).body("id", Matchers.equalTo(1), new Object[0]);
    }
    @Test
    @Order(3)
    public void testCreatePost() {
        ((ValidatableResponse)((ValidatableResponse)((Response)RestAssured.given().contentType("application/json").body("{ \"title\":  \"New Post\", \"content\":  \"This is a test post\"}").when().post("/posts", new Object[0])).then()).statusCode(201)).body("title", Matchers.equalTo("New Post"), new Object[0]);
    }
    @Test
    @Order(4)
    public void testDeletePost() {
        ((ValidatableResponse)((Response)RestAssured.given().pathParams("id", 1, new Object[0]).when().delete("/posts/{id}", new Object[0])).then()).statusCode(Matchers.anyOf(Matchers.is(200), Matchers.is(202), Matchers.is(204), Matchers.is(404)));
    }

    @Order(5)
    public void testUpdatePost() {
        ((ValidatableResponse)((ValidatableResponse)((Response)RestAssured.given().contentType("application/json").pathParams("id", 1, new Object[0]).body("{\"title\":  \"Update Post\", \"content\":  \"Update content\"}").when().put("/posts/{id}", new Object[0])).then()).statusCode(200)).body("title", Matchers.equalTo("Update Post"), new Object[0]);
    }
    @Test
    @Order(6)
    public void testCommentsForPost() {
        ((ValidatableResponse)((ValidatableResponse)((Response)RestAssured.given().when().get("/posts/1/comments", new Object[0])).then()).statusCode(200)).body("$.size()", Matchers.greaterThan(0), new Object[0]);
    }
    @Test
    @Order(7)
    public void testGetCommentsPostsIdQueryParam() {
        ((ValidatableResponse)((ValidatableResponse)((Response)RestAssured.given().queryParam("postId", new Object[]{1}).when().get("/comments", new Object[0])).then()).statusCode(200)).body("[0].postId", Matchers.equalTo(1), new Object[0]);
    }
}
