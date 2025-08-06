

import com.fasterxml.jackson.annotation.JsonFormat;
import jakarta.persistence.*;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.Async;

import java.time.LocalDateTime;


@Data
@Slf4j
@Entity
@Getter
@Setter
@Table(name = "dht")
@NoArgsConstructor
@Async
public class DHTModel {


    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    private String location;
    private double temperature;
    private double humidity;
    @JsonFormat(pattern = "yyyy-MM-dd'T'HH:mm:ss")
    private LocalDateTime date;

    public DHTModel(double temperature, double humidity, LocalDateTime date, String location) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.date = date;
        this.location = location;
    }
}
