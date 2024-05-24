from pathlib import Path
from pprint import pformat

from hloc import extract_features, match_features, pairs_from_covisibility, pairs_from_retrieval
from hloc import colmap_from_nvm, triangulation, localize_sfm, visualization

def main():
    # Our Dataset - new-7sec
    # dataset = Path('C:/Users/unist/Desktop/KETI-Code/Hierarchical-Localization/datasets/7sec')
    # images = dataset / 'ref/'
    # images_query = dataset / 'query/'

    # SPED
    # dataset = Path('C:/Users/unist/Desktop/KETI-Code/VPR-datasets-downloader/datasets/sped/images/test')
    # images = dataset / 'database/'
    # images_query = dataset / 'queries/'

    # Synthetia
    dataset = Path('C:/Users/unist/Desktop/KETI-Code/OpenDataset/2SALAD/5Synthia-NightToFall')
    images = dataset / 'ref_new/'
    images_query = dataset / 'query_new/'

    outputs = Path('C:/Users/unist/Desktop/KETI-Code/Hierarchical-Localization/outputs')
    sfm_pairs = outputs / 'pairs-factory.txt'
    loc_pairs = outputs / 'pairs-query-factory.txt'
    print(f'Configs for feature extractors:\n{pformat(extract_features.confs)}')
    print(f'Configs for feature matchers:\n{pformat(match_features.confs)}')

    retrieval_netvlad_conf = extract_features.confs['netvlad']
    retrieval_ibl_conf = extract_features.confs['openibl']
    retrieval_eigen_conf = extract_features.confs["eigenplaces"]

    feature_conf = extract_features.confs['superpoint_aachen']
    matcher_conf = match_features.confs['superglue']

    # retrieval 변수명 수정 (NetVlad, Openibl, Eigenplaces)

    # DB 이미지에서 global descriptor 추출
    db_global_descriptors = extract_features.main(retrieval_netvlad_conf, images, outputs)
    # db_global_descriptors = extract_features.main(retrieval_ibl_conf, images, outputs)
    # db_global_descriptors = extract_features.main(retrieval_eigen_conf, images, outputs)
   
    # Query 이미지에서 global descriptor 추출
    # db_global_descriptors = extract_features.main(retrieval_netvlad_conf, images_query, outputs)
    # db_global_descriptors = extract_features.main(retrieval_ibl_conf, images_query, outputs)
    # db_global_descriptors = extract_features.main(retrieval_eigen_conf, images_query, outputs)

if __name__ == "__main__":
    main()

