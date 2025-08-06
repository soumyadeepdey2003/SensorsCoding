import com.trex.iot_backend.model.DHTModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface DHTRepository extends JpaRepository<DHTModel, Long> {
}
