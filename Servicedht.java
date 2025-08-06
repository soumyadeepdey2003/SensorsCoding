import com.trex.iot_backend.Repository.DHTRepository;
import com.trex.iot_backend.model.DHTModel;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
@Slf4j
@RequiredArgsConstructor
public class DHTService {

    @Autowired
    private DHTRepository dhtRepository;

    public DHTModel save(DHTModel dhtModel)throws Exception {
        LocalDateTime now = LocalDateTime.now();
        dhtModel.setDate(now);
        log.info("Saving DHTModel {}", dhtModel);
        try {
            return dhtRepository.save(dhtModel);
        } catch (Exception e) {
            log.error("Error saving DHTModel {}", dhtModel, e);
            throw new Exception("Error saving DHTModel");
        }

    }

    public List<DHTModel> findAll()throws Exception {
        log.info("Finding all DHTModels");
        try {
            List<DHTModel> dhtModels = dhtRepository.findAll();
            return dhtModels;
        } catch (Exception e) {
            log.error("Error finding DHTModels", e);
            throw new RuntimeException("Error finding DHTModels");
        }
    }

    public void deleteAll() {
        log.info("Deleting all DHTModels");
        dhtRepository.deleteAll();
    }

    public void delete(DHTModel dhtModel) {
        log.info("Deleting DHTModel {}", dhtModel);
        dhtRepository.delete(dhtModel);
    }

    public Optional<DHTModel> finddhtbyid(long id)throws Exception {
        Optional<DHTModel> optionalDHT = dhtRepository.findById(id);

        if (optionalDHT.isPresent()) {
            log.info("Found DHTModel by id {}", id);
            return optionalDHT;
        } else {
            log.warn("DHTModel not found for id {}", id);
            throw new RuntimeException("DHTModel not found");
        }
    }

}
