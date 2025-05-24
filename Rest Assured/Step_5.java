import com.fasterxml.jackson.databind.util.JSONPObject;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.json.JSONObject;

import static io.restassured.RestAssured.given;

public class Step_5 {

    private static final String BASE_PATH = "/posts/{id}";

    @BeforeEach
    public void setUp() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com/";
    }

    private Response updatePost(Object postId, JSONObject requestBody, String method) {
        return given()
                .contentType(ContentType.JSON)
                .body(requestBody.toString())
                .pathParams("id", postId)
                .when()
                .request(method, BASE_PATH)
                .then()
                .extract()
                .response();
    }

    @ParameterizedTest
    @CsvSource({
            "1, Update Title, Update Body, 1, PUT, Update Title",
    })

    void updatePostParameter(Object postId,String title, String body, Object userId, String method, String resTitle ){
        JSONObject requestBody = new JSONObject();
        if(title != null && !title.isEmpty()) {
            requestBody.put("title", title);
        }
        if (body != null && !body.isEmpty()) {
            requestBody.put("body", body);
        }
        if(userId != null && !userId.toString().isEmpty()) {
            requestBody.put("userId", userId);
        }

        Response response = updatePost(postId, requestBody, method);
            Assertions.assertEquals(200, response.getStatusCode());
            if(resTitle != null && !resTitle.isEmpty()) {
                Assertions.assertEquals(resTitle, response.jsonPath().getString("title"));
            }
        };
    @Test
    void updatePostWidthStringId(){
        JSONObject requestBody = new JSONObject();
        requestBody.put("title", "String ID");
        Response response = updatePost("abc", requestBody, "PUT");
        Assertions.assertEquals(500, response.getStatusCode());
    }
    }


