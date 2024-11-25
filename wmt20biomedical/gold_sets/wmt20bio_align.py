
import os

def load_mapping(mapping_file):
	mapping = {}
	with open(mapping_file, 'r') as in_file:
		for line in in_file:
			pmid, mapid = line.strip().split("\t")
			mapping[mapid] = pmid
	return mapping

def load_align_validation_file(align_validation_file):
	alignment = {}
	bck_pmid = None
	index = 0
	with open(align_validation_file, 'r') as in_file:
		for line in in_file:
			print(line)
			validation, pmid, sents_x, sents_en = line.strip().split("\t")
			if "," in sents_x:
				sents_x = sents_x.split(",")
			else:
				sents_x = [sents_x]
			if "," in sents_en:
				sents_en = sents_en.split(",")
			else:
				sents_en = [sents_en]
			if not bck_pmid==pmid:
				index = 0
				bck_pmid = pmid
				alignment[pmid] = {}
			alignment[pmid][index] = {}
			alignment[pmid][index]["x"] = sents_x
			alignment[pmid][index]["en"] = sents_en
			alignment[pmid][index]["validation"] = validation
			index += 1
	#print(data)
	return alignment

def load_testset_file(testset_file,mapping):
	testset = {}
	bck_pmid = None
	with open(testset_file, 'r') as in_file:
		for line in in_file:
			docid, sent_id, text = line.strip().split("\t")
			pmid = mapping[docid]
			if not bck_pmid==pmid:
				bck_pmid = pmid
				testset[pmid] = {}
			testset[pmid][sent_id] = text
	return testset

def create_aligned_file(dataset,lang,testset_file,align_validation_file,mapping_file,out_dir):
	mapping = load_mapping(mapping_file)
	alignment = load_align_validation_file(align_validation_file)
	testset = load_testset_file(testset_file,mapping)
	for pmid in testset:
		print(pmid)
		print(testset[pmid])
		with open(os.path.join(out_dir,dataset+"_"+pmid+"_"+lang+".txt"), "w") as writer:
			for align_item in alignment[pmid]:
				if not alignment[pmid][align_item]["validation"]=="OK":
					continue
				if lang=="en":
					sents = alignment[pmid][align_item]["en"]
				else:
					sents = alignment[pmid][align_item]["x"]
				text = ""
				for sent_num in sents:
					if sent_num=="omitted":
						text += " "
					else:
						text += testset[pmid][sent_num]+" "
				text = text.strip()
				#print(pmid,align_item,text)
				writer.write(text+"\n")
			writer.close()

if __name__ == '__main__':
	alignment_dir = "alignment_files/"
	mapping_dir = "docid_mapping_files/"
	gold_test_dir = "gold_test_files/"
	out_dir = "out/" # user-defined
	align_validation_file = alignment_dir+"zh-en_align_validation.tsv"
	mapping_file = mapping_dir+"zhen_mapping.txt"
	#create_aligned_file("en2zh","en",gold_test_dir+"medline_en2zh_en.txt",align_validation_file,mapping_file,out_dir)
	create_aligned_file("en2zh","zh",gold_test_dir+"medline_en2zh_zh.txt",align_validation_file,mapping_file,out_dir)
	#create_aligned_file("zh2en","zh",gold_test_dir+"medline_zh2en_zh.txt",align_validation_file,mapping_file,out_dir)
	create_aligned_file("zh2en","en",gold_test_dir+"medline_zh2en_en.txt",align_validation_file,mapping_file,out_dir)

